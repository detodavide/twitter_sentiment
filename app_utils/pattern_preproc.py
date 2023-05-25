import re

def clean_text(text, patterns):

    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    text = text.lower().strip()
    return [text]

def preprocess(input):

    patterns = {
            r"UTC]": ' ',
            r"b'": ' ',
            r'\d+': ' ',      # rimuove digits (numeri)
            r'[^\w\s]': ' ',  # Remove punteggiatura e simboli ...,'@!£$%
            r'\b\w{1,2}\b':' ',#remove all token less than2 characters
            r'(http|www)[^\s]+':' ', # remove website
            r' one ': ' ',
            r' will ': ' ',
            r' new ': ' ',
            r' amp ': ' ',
            r'\s+': ' '    # rimuove tutti i multipli spazi con uno spazio
            }
    
    if isinstance(input, str):
        cleaned_text = clean_text(input, patterns)
        return cleaned_text
