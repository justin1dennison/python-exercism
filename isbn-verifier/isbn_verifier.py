import string

def verify(isbn):
    isbn = isbn.replace("-", "")
    invalid_chars = string.ascii_uppercase.replace("X", "")
    has_no_invalid_chars = all(not c in isbn for c in invalid_chars)
    has_correct_length = len(isbn) == 10
    has_correct_sum = sum(((10 - i) * int(c) 
                                if c != "X"  and c not in invalid_chars
                                else 10
                                for i, c in enumerate(isbn))
                        )  % 11  == 0

    return (has_no_invalid_chars and 
            has_correct_length and 
            has_correct_sum)
