filename = input("Enter the filename to read and modify: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    file.close()

    new_file = open(filename, 'w')
    new_file.write("modified_content")
    print(new_file)


except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except IOError:
    print("❌ Error: The file could not be read or written.")
