from string import ascii_letters
import re

def hey(phrase):
    phrase = phrase.strip(' ')
    if is_silent(phrase):
        return "Fine. Be that way!"
    elif is_question(phrase) and is_yelling(phrase):
        return "Calm down, I know what I'm doing!"
    elif is_yelling(phrase):
        return "Whoa, chill out!"
    elif is_question(phrase):
        return "Sure."
    else:
        return "Whatever."

def is_question(s):
    return s.endswith("?")

def is_yelling(s):
    return s.upper() == s and any(c in ascii_letters for c in s)

def is_silent(s):
    exp = re.compile("[\t\r\n ]")
    return exp.sub("", s) == ""
