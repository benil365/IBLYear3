def main():
    # Prompt the user to enter some text
    text = input("Text: ")

    # Count the number of times "um" appears in the text
    um_count = count(text)

    # Print the result
    print(f"\"um\" appears {um_count} time(s) in the text.")
def count(s):
    # Split the input string into words
    words = s.split()

    # Initialize a counter
    count = 0

    # Iterate over the words
    for word in words:
        # Check if the word is "um" or "Um" (case-insensitive)
        if word.lower() == "um":
            count += 1

    # Return the count
    return count
