import re

def convert_number_words(string):
    # Define a dictionary to map number words to their numeric values
    number_words = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
        'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90, 'hundred': 100
    }
    
    # Create a regular expression pattern to match number words
    pattern = re.compile(r'\b(' + '|'.join(number_words.keys()) + r')\b')
    
    # Find all matches in the string and replace them with their numeric values
    matches = pattern.findall(string)
    for match in matches:
        numeric_value = number_words[match]
        string = re.sub(r'\b' + match + r'\b', str(numeric_value), string)
    
    return string

# Example usage
text = "I have one hundred twenty apples and fifty two oranges."
converted_text = convert_number_words(text)
print(converted_text)
