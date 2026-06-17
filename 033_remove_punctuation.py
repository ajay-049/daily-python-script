import string

def remove_punctuation(text):
    # Create a translation table that maps all punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the table to remove punctuation from the string
    return text.translate(translator)

# Example usage
input_string = "Hello, World! Welcome to Python... right?"
cleaned_string = remove_punctuation(input_string)

print("Original:", input_string)
print("Cleaned :", cleaned_string)
