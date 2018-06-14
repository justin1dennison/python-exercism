import string

def verify(isbn):
    isbn = isbn.replace("-", "")
    if any(c in isbn for c in string.ascii_uppercase.replace("X", "")):
        return False
    if len(isbn) != 10:
        return False
    return sum(
        ((10 - i) * int(c) 
            if c != "X" 
            else 10
            for i, c in enumerate(isbn))
    )  % 11 == 0
