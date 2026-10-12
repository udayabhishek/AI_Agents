from openai import OpenAI
from similarity import consine_similarity

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama"
)

sentence1 = "Python is a programming language"
response = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence1
)

embedding1 = response.data[0].embedding
print(type(embedding1))
print(len(embedding1))

sentence2 = "python is a coding language used in web development"
response = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence2
)

embedding2 = response.data[0].embedding
print(type(embedding2))
print(len(embedding2))

sentence3 = "Swift is a programming language"

response = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence3
)

embedding3 = response.data[0].embedding
print(type(embedding3))
print(len(embedding3))

sentence4 = "pizza is delicious"

response = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence4
)

embedding4 = response.data[0].embedding
print(type(embedding4))
print(len(embedding4))

score12 = consine_similarity(embedding1, embedding2)
print(score12)

score14 = consine_similarity(embedding1, embedding4)
print(score14)



def create_embedding(content):
    embedding1 = client.embeddings.create(
        model = "nomic-embed-text",
        input = content).data[0].embedding

    return embedding1

