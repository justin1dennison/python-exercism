import re
from collections import Counter
import string as s

def is_isogram(string):
    exp = re.compile(f"[{s.punctuation} ]")
    lowercase = string.lower()
    sanitized = exp.sub("", lowercase)
    counter = Counter(sanitized)
    return all(
        (v == 1 for _, v in counter.items())         
    )
