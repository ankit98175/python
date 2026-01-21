# ---------------------------------------------------task - 1---------------------------->

try:
    file = open("sample.txt", "r")
    print("Reading file content:\n")

    for line in file:
        print(line, end="")

    file.close()

except FileNotFoundError:
    print("Error: sample.txt file does not exist.")
    
else:
    print("\nFile read successfully.")


# ---------------------------------------------------task - 2 ---------------------------->



text = input("Enter text to write in file: ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()


more_text = input("Enter text to append in file: ")

file = open("output.txt", "a")
file.write(more_text + "\n")
file.close()


print("\nFinal content of the file:")

file = open("output.txt", "r")
print(file.read())
file.close()
