from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool
from tools import read_text

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

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice : ")

messages = [
    {
        "role": "system",
        "content": roles.get(choice, "You are a friendly AI assistant. Provide helpful and informative responses.")
    }
]

while True:
    user_input = input("\nYou: ")

    text = user_input.lower()

    if text.startswith("summerize "):
        filename = user_input[10:].strip()
        file_content = read_text("data/" + filename)
        prompt = f"""
        summerize the following document.
        Document:
        {file_content}
        """

        response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = [
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )

        print(response.choices[0].message.content)
        continue


    if text.startswith("explain "):
        filename = user_input[8:].strip()
        file_content = read_text("data/" + filename)
        prompt = f"""
        explain the following document in simple language with real-life examples.
        Document:
        {file_content}
        """

        response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = [
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )

        print(response.choices[0].message.content)
        continue


    if text.startswith("ask"):
        parts = user_input.split(maxsplit=2)
        print(parts)

        filename = parts[1]
        question = parts[2]

        file_content = read_text(
            "data/" + filename
        )

        prompt = f"""
            You are given a document.

            Answer the user's question using only the information present in the document.

            If the answer is not available, say:
            'I couldn't find that information in the document.'

            Document:

            {file_content}

            Question:

            {question}
            """

        response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = [
                {
                    "role": "system",
                    "content": "you are a helpful assistent"

                },
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )

        print(response.choices[0].message.content)
        continue



    tool_result = execute_tool(user_input)

    if tool_result:
        print(f"\nAI: {tool_result}")
        continue

    messages.append(
        {
            "role": "user", 
            "content": user_input
        }
    )


    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break   

    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = messages
    )

    ai_response = response.choices[0].message.content

    print("\nAI :", ai_response)

    messages.append(
        {
            "role": "assistant", 
            "content": ai_response
        }
    )