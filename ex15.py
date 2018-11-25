# imports argv from sys library
from sys import argv

# telling the code that it has 2 arguments
script, filename = argv

# assigning the txt variable to the opened file
txt = open(filename)

# printing the filename and its contents
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

# repeating
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
