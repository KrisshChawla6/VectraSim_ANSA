#
# ANSA Python Script Agent (WIP)
# - Uses OpenAI GPT to generate ANSA Python scripts from user prompts
# - Parses ANSA Python API to extract functions and docstrings
#
# **WIP, not functional yet**
#
# ==========================

import os
import ast
from openai import OpenAI
from typing import List, Dict, Any
from dotenv import load_dotenv


# ==========================
# CONFIG
# ==========================
load_dotenv()

BASE_PATH = "./pydev_ansa/ansa"  # Folder containing base.py, mesh.py, etc.
OPENAI_MODEL = "gpt-4.1-nano (long context)"  # Or gpt-4o / gpt-4-turbo
# api_key = os.environ.get("OPENAI_API_KEY")
api_key = "API_KEY"
client = OpenAI(api_key=api_key)


# ==========================
# STEP 1 — PARSE API STUBS
# ==========================
def parse_ansa_api(base_path: str) -> List[Dict[str, Any]]:
    api_data = []

    def parse_file(file_path, module_path):
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                func_info = {
                    "module": module_path,
                    "name": node.name,
                    "signature": f"{node.name}({', '.join(arg.arg for arg in node.args.args)})",
                    "args": [arg.arg for arg in node.args.args],
                    "docstring": ast.get_docstring(node) or "",
                }
                api_data.append(func_info)

            elif isinstance(node, ast.ClassDef):
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef):
                        func_info = {
                            "module": f"{module_path}.{node.name}",
                            "name": subnode.name,
                            "signature": f"{subnode.name}({', '.join(arg.arg for arg in subnode.args.args)})",
                            "args": [arg.arg for arg in subnode.args.args],
                            "docstring": ast.get_docstring(subnode) or "",
                        }
                        api_data.append(func_info)

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_path)
                module_path = "ansa." + rel_path.replace(os.sep, ".").replace(".py", "")
                parse_file(file_path, module_path)

    return api_data


# ==========================
# STEP 2 — CONVERT TO FUNCTION SCHEMA
# ==========================
def convert_to_openai_functions(api_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    functions = []
    for func in api_data:
        params = {"type": "object", "properties": {}, "required": []}
        for arg in func["args"]:
            params["properties"][arg] = {
                "type": "string",
                "description": f"Argument '{arg}' for {func['module']}.{func['name']}",
            }
            params["required"].append(arg)

        functions.append(
            {
                "name": f"{func['module'].replace('.', '_')}_{func['name']}",
                "description": func["docstring"][:300]
                + ("..." if len(func["docstring"]) > 300 else ""),
                "parameters": params,
            }
        )
    return functions


# ==========================
# STEP 3 — GPT AGENT
# ==========================
def ask_gpt_to_generate_script(user_request: str, api_data: list) -> str:
    # Simple retrieval: inject all API docstrings (can optimize later)
    api_context = "\n".join(
        [f"{f['module']}.{f['signature']}\n{f['docstring']}" for f in api_data]
    )

    system_prompt = f"""
You are an expert Python automation assistant that writes ANSA scripts.
You must follow exactly the ANSA API functions provided below.
Do not invent new functions. Only use those listed.

Available API methods:
{api_context}
    """

    # encoding = tiktoken.encoding_for_model("gpt-4.1-nano")
    # num_tokens = len(encoding.encode(system_prompt)) + len(encoding.encode(user_prompt))
    # print(f"Total tokens in request: {num_tokens}")

    completion = client.chat.completions.create(
        model=OPENAI_MODEL,  # or gpt-4o, gpt-4-turbo
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request},
        ],
        temperature=0,
    )

    return completion.choices[0].message.content


# ==========================
# STEP 4 — VALIDATE SCRIPT
# ==========================
def validate_script(script: str, api_data: List[Dict[str, Any]]) -> List[str]:
    allowed_funcs = {
        f"{item['module']}.{item['name']}": item["args"] for item in api_data
    }
    errors = []

    try:
        tree = ast.parse(script)
    except SyntaxError as e:
        return [f"Syntax error: {e}"]

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and isinstance(
                node.func.value, ast.Attribute
            ):
                # e.g., ansa.base.CollectEntities()
                full_name = f"{node.func.value.attr}.{node.func.attr}"
            elif isinstance(node.func, ast.Attribute) and isinstance(
                node.func.value, ast.Name
            ):
                # e.g., base.CollectEntities()
                full_name = f"{node.func.value.id}.{node.func.attr}"
            elif isinstance(node.func, ast.Name):
                full_name = node.func.id
            else:
                continue

            # Match against API methods
            matches = [k for k in allowed_funcs if k.endswith(full_name)]
            if not matches:
                errors.append(f"Function not allowed: {full_name}")
            else:
                expected_args = allowed_funcs[matches[0]]
                call_arg_count = len(node.args)
                if call_arg_count != len(expected_args):
                    errors.append(
                        f"Arg mismatch in {full_name}: expected {len(expected_args)}, got {call_arg_count}"
                    )

    return errors


def prompt_user_multiline(prompt_label="ansa> "):
    """
    Read a multiline user prompt from the terminal.
    User types lines; submitting a blank line (press Enter on a blank line)
    ends input and returns the combined text.
    Provides simple readline history/navigation.
    """
    print(
        "Enter ANSA instruction. Finish with an empty line (press Enter on a blank line):\n"
    )
    lines = []
    try:
        while True:
            line = input(prompt_label)
            # If user presses blank line and there's at least one line, finish
            if line.strip() == "" and lines:
                break
            # If user presses blank line as first line, continue (no input yet)
            if line.strip() == "" and not lines:
                continue
            lines.append(line)
    except (EOFError, KeyboardInterrupt):
        # Graceful exit on Ctrl-D / Ctrl-C
        print()
    return "\n".join(lines)


# ==========================
# MAIN PIPELINE
# ==========================
if __name__ == "__main__":
    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("Parsing ANSA API...")
    api_data = parse_ansa_api(os.path.join(script_dir, BASE_PATH))
    print(f"Found {len(api_data)} functions.")

    # user_prompt = prompt_user_multiline()
    # print("\n--- Received prompt ---")
    # print(user_prompt)

    user_prompt = "First collect all the faces. Then use the faces to generate a mid surface mesh. Set thick=1.0"

    print("\nGenerating script from GPT...")
    script = ask_gpt_to_generate_script(user_prompt, api_data)
    print("\n--- Generated Script ---\n")
    print(script)

    print("\nValidating script...")
    errors = validate_script(script, api_data)
    if errors:
        print("Validation errors found:")
        for err in errors:
            print(" -", err)
    else:
        print("✅ Script is valid according to ANSA API.")
