from retriever import retriever

filename, content = retriever("Python")

print(filename)
print()
print(content)
print("-"*40)
    

filename, content = retriever("programming language")
print(filename)
print()
print(content)
print("-"*40)

filename, content = retriever("coding language")
print(filename)
print()
print(content)
print("-"*40)

filename, content = retriever("database")
print(filename)
print()
print(content)
print("-"*40)

filename, content = retriever("wind")
print(filename)
print()
print(content)
print("-"*40)

filename, content = retriever("artificial")
print(filename)
print()
print(content)
print("-"*40)