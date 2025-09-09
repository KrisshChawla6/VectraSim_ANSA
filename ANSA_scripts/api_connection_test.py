# Gemini API connection test script

import ssl
import requests

API_KEY = "AIzaSyA9oddVciKKYo12yfLumVjmC9NmdAZLIcg"
MODEL = "models/gemini-2.5-pro"
url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent"
headers = {"Content-Type": "application/json"}
params = {"key": API_KEY}
data = {"contents": [{"parts": [{"text": "Hello, Gemini 2.5 Pro!"}]}]}

ssl_context = ssl.create_default_context()
ssl_context.set_ciphers("DEFAULT@SECLEVEL=1")

response = requests.post(url, headers=headers, params=params, json=data, verify=True)
print("Status code:", response.status_code)
print("Response:", response.json())
