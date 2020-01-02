import re
from string import punctuation

pattern = f'({"|".join(re.escape(letter) for letter in punctuation)})'
SPACE = ' '
EMPTY = ''
SINGLE_QUOTE = '\''

def clean(words):
    without_single_quote = re.sub(SINGLE_QUOTE, EMPTY, words)
    return re.sub(pattern, SPACE, without_single_quote) 

def abbreviate(words):
    cleaned = clean(words)
    split = (word for word in cleaned.split(SPACE) if word)
    first = (f for f, *rest in split)
    return EMPTY.join(letter.upper() for letter in first)

