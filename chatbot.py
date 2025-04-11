import os
import requests

# Cloudflare Worker proxy URL
WORKER_URL = "https://openai-worker.rish-worker.workers.dev"

# Format the full prompt to include role instructions
def format_prompt(user_input):
    return (
        "You are a professional financial analyst. "
        "You specialize in market trends, earnings reports, and investment strategy. "
        "You always answer with concise and well-reasoned insights, and avoid speculation when uncertain.\n\n"
        f"User: {user_input}\n"
        "Financial Analyst:"
    )

# Sends the prompt to the Cloudflare Worker (which relays to OpenAI)
def ask_openai(prompt):
    try:
        response = requests.post(WORKER_URL, json={"prompt": format_prompt(prompt)})
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# CLI loop
def main():
    print("💬 FinGPT (Financial Analyst Chatbot) — type 'exit' to quit")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        reply = ask_openai(user_input)
        print("🤖", reply)

if __name__ == "__main__":
    main()
