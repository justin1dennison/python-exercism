sounds = (("Pling", 3), ("Plang", 5), ("Plong", 7))


def convert(number):
    result = "".join(word for word, divisor in sounds if number % divisor == 0)
    return result or str(number)
