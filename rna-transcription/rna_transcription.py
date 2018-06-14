def to_rna(dna_strand):
    lookup = dict(G='C', C='G', T='A', A='U')
    return ''.join(lookup.get(c, c) for c in dna_strand)
