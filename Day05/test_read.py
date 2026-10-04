def read_text(text_file):
    try:
        with open(text_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{text_file}' was not found."
    

print(read_text('data/text_file.txt'))


def read_shopping(txt_file):

    try: 
        with open(txt_file, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: {txt_file} not found in the dir"

    
print(read_shopping("data/shopping_list.txt"))
