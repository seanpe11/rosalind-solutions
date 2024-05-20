dna = input()

dna_dict = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0,
}

for x in dna:
    dna_dict[x] += 1

print(dna_dict)
