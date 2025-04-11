import os
import requests
from dotenv import load_dotenv

load_dotenv()
WORKER_URL = os.getenv("CF_WORKER_URL")

def ask_openai(prompt):
    try:
        response = requests.post(WORKER_URL, json={"prompt": prompt})
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

def main():
    print("💬 Personal Finance AI Assitant — type 'exit' to quit")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        response = ask_openai(user_input)
        print("🤖", response)

if __name__ == "__main__":
    main()

