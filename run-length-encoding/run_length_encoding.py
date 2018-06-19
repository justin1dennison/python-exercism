from itertools import groupby
import re

decoder = re.compile(r'\d{0,2}[a-zA-Z ]{1}')

def decode(string):
    string_parts = ((m[-1], m[:-1]) for m in decoder.findall(string))
    results = (int(count or 1) * letter 
                for letter, count in string_parts)
    return ''.join(results)
    

def encode(string):
    counts = ((letter, len(list(group))) for letter, group in groupby(string))
    return ''.join(f"{count}{letter}" 
                if count > 1
                else f"{letter}"
                for letter, count in counts)

