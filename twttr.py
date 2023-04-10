def remove_vowels(text):
    """
    The function removes all vowels from a given text input.
    
    :param text: The input text that the user enters
    :return: The function `remove_vowels` returns the input text with all vowels removed.
    """
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text

text = input("Enter some text: ")
text_without_vowels = remove_vowels(text)
print(text_without_vowels)