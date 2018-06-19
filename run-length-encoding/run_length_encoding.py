from itertools import groupby
import re

decoder = re.compile(r'\d{0,2}[a-zA-Z ]{1}')

def decode(string):
    if not string:
        return string
    matches = decoder.finditer(string)
    groups = (m.group() for m in matches)
    string_parts = ((g[-1], g[:-1]) for g in groups)
    results = (int(count) * letter 
                if count 
                else letter
                for letter, count in string_parts)
    return ''.join(results)
    

def encode(string):
    if not string:
        return string
    letter_counts = [(letter, len(list(group))) 
                        for letter, group in groupby(string)]
    return ''.join(f"{count}{letter}" 
                if count > 1 
                else f"{letter}"
                for letter, count in letter_counts)
