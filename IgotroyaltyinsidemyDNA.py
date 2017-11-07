'''Julia Marden and Jack Obrock
9/20/17'''
dna = input('What sequence of dna do you want to test? ')
def get_length(dna):
    if dna == '':
        return 0
    return 1 + get_length(dna[1:])
print(get_length(dna))

def is_valid_sequence(dna):
    if dna == '':
        return True
    elif dna[0] == 'A' or dna[0] == 'T' or dna[0] == 'C' or dna[0] == 'G':
        is_valid_sequence(dna[1:])
    else:
        return False

nucleotide = input('Which nucleotide do you want to count? ')
def count_nucleotides(dna, nucleotide):
    if dna=='':
        return 0
    elif dna[0] == nucleotide:
        return 1 + count_nucleotides(dna[1:], nucleotide)
    return 0 + count_nucleotides(dna[1:], nucleotide)
print(count_nucleotides(dna, nucleotide))

dna1 = input('What is your first strand of dna? ')
dna2 = input('What is your second strand of dna? ')
def is_longer(dna1,dna2):
    if get_length(dna1) > get_length(dna2):
        return True
    return False
print(is_longer(dna1,dna2))

def get_complement(nucleotide):
    base_complement = {'A':'T','C':'G','G':'C','T':'A'}
    return base_complement[nucleotide]
print(get_complement(nucleotide))

def get_complementary_strand(dna):
    if dna == '':
        return ''
    else:
        return get_complement(dna[0]) + get_complementary_strand(dna[1:])
print(get_complementary_strand(dna))