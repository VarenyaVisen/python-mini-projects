from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("GROQ_API_KEY")

messages = []
client = Groq(api_key=api)


def completion(message):
    global messages
    messages.append(
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": message,
        }

    )

    # Move the chat completion inside the function
    chat_completion = client.chat.completions.create(
        messages=messages,
        # The language model which will generate the completion.
        model="llama-3.3-70b-versatile"
    )

    # Process the response
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message['content']}")


if __name__ == "__main__":
    print(f"Jarvis : Hi I am Jarvis, How can I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)
