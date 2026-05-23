try:
   
    with open('test.txt', 'w') as file:
        file.write("This is a test file.")
    with open('test.txt', 'r') as file:
        print(file.read())
    with open('test.txt', 'r+') as file:
        print(file.read())
    with open('test.txt', 'a') as file:
        text=file.write("123")
        print(text)
    with open('test.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file 'test.txt' was not found.")
