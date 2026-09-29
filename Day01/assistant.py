from openai import OpenAI
from dotenv import load_dotenv
import os

#load configuration from .env file
load_dotenv()

# Create a client that communicates with the Ollama API
client = OpenAI(
    base_url=os.getenv("BASE_URL"), 
    api_key=os.getenv("API_KEY"),
    # model=os.getenv("MODEL")
)   

print("=" *40)
print("My AI Assistant")
print("=" *40)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break   

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user", 
                "content": user_input
            }
        ]
    )

    print("\nAI: ", response.choices[0].message.content)