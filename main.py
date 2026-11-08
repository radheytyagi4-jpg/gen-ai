
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key")
)

# Conversation memory
messages = []

# AI personality
SYSTEM_PROMPT = """
You are Nova, a helpful AI assistant.
You are friendly, intelligent and good at explaining
programming concepts in simple language.
"""

def chat(user_message):

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.responses.create(
        model="gpt-6-astra",
        instructions=SYSTEM_PROMPT,
        input=messages
    )

    ai_reply = response.output_text

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    return ai_reply


def main():

    print("\n================================")
    print("       NOVA AI TERMINAL")
    print("================================")
    print("Your personal AI assistant")
    print("Type /exit to quit")
    print("Type /clear to clear memory")
    print("--------------------------------\n")

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "/exit":
            print("Nova: Goodbye!")
            break

        if user_input.lower() == "/clear":
            messages.clear()
            print("Nova: Conversation cleared!")
            continue

        try:
            print("\nNova: ", end="", flush=True)

            answer = chat(user_input)

            print(answer)

        except Exception as error:
            # Remove the failed user message
            if messages and messages[-1]["role"] == "user":
                messages.pop()

            print(f"\nError: {error}")

        print()


if __name__ == "__main__":
    main()
