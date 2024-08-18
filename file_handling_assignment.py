try:
    # file creation
    with open('my_file', 'w') as file:
        file.write("Hello, world!\n")
        file.write("The number is 42.\n")
        file.write("Python is fun!\n")

    # file reading and display
    with open('my_file', 'r') as file1:
        print(file1.read())


    # file appending
    with open('my_file', 'a') as file:
        file.write("Appending new line 1.\n")
        file.write("Appending new line 2 with number 100.\n")
        file.write("Appending new line 3. Python is great!\n")


except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have the necessary permissions to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")