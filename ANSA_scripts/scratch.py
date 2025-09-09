# PYTHON script
import os
import ansa


def main():
    # Need some documentation? Run this with F5

    help_html = os.path.join(
        ansa.constants.app_root_dir.replace("/", os.path.sep),
        "..",
        "ansa_v25.1.2",
        "docs",
        "extending",
        "python_api",
        "html",
        "index.html",
    )
    print("Documentation HTML: " + help_html)

    ansa.base.All()

    print(ansa.base.CurrentDeck())
    print(ansa.base.CollectEntities(ansa.base.CurrentDeck(), None, "SHELL", True))


if __name__ == "__main__":
    main()
