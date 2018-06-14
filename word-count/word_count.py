from collections import Counter
from string import punctuation

def replace(chars, with_what, text):
    for char in chars:
        text = text.replace(char, with_what)
    return text


def word_count(phrase):
    splits = (',', '_')
    specials = ("\n", "\t")
    puncts = replace(("'", "_", ","), "", punctuation)
    phrase = replace(puncts, "", phrase)
    phrase = phrase.lower()
    phrase = replace(splits, " ", phrase)
    phrase = replace(specials, " ", phrase)
    words = phrase.split(" ") 
    return dict(Counter(word.replace("'", "") 
                        if word.startswith("'") 
                        else word 
                        for word in words if word))    


