from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from .env file
load_dotenv()

# Create a client that communicates with the Ollama API
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
    # model=os.getenv("MODEL")
)

# Send a question to the AI Model and get a response
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user", 
            "content": "What is a Artificial Intelligence?"
        }
    ]
)

# Display the response from the AI Model
print(response.choices[0].message.content)

