scores = (
    (set("aeioulnrst"), 1),
    (set("dg"), 2),
    (set("bcmp"), 3),
    (set("fhvwy"), 4),
    (set("k"), 5),
    (set("jx"), 8),
    (set("qz"), 10),
)

lookup = dict((letter, value) for letters, value in scores for letter in letters)


def score(word):
    return sum(lookup[letter] for letter in word.lower())
