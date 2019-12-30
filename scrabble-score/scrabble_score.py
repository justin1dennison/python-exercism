letter_values = [
    (set("aeioulnrst"), 1),
    (set("dg"), 2),
    (set("bcmp"), 3),
    (set("fhvwy"), 4),
    (set("k"), 5),
    (set("jx"), 8),
    (set("qz"), 10),
]


def score(word):
    return sum(value for letter in word for st, value in letter_values if letter.lower() in st)
