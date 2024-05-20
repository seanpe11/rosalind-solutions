# https://rosalind.info/problems/revc/

dna = input()

reverse_complement = ''
complements = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

for x in range(0, len(dna)):
    reverse_complement = reverse_complement + (complements[dna[x]])

print(reverse_complement[::-1])
