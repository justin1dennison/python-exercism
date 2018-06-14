def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands must be of equal length")
    if strand_a == strand_b:
        return 0
    return sum(1 if a != b else 0 for a,b in zip(strand_a, strand_b))
