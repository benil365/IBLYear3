# This code prompts the user to enter their name using the `input()` function and stores the input in
# the variable `name`. Then, it opens a file called "names.txt" in append mode using the `open()`
# function and writes the value of `name` to the file using the `write()` method. The `\n` character
# is added to the end of the name to ensure that each name is written on a new line. Finally, the file
# is closed using the `close()` method. This code essentially allows the user to add their name to a
# list of names stored in a file.
name = input("Whats your name:")
with open("names.txt", "a") as file:
   file.write(f"{name}\n")

file.close()