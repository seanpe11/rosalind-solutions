from util.rna_codon_table import codon_table 

hello = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
out = ""

for x in range(0, len(hello), 3):
    substr = hello[x:x+3]
    if (codon_table[substr] == "Stop"):
        break
    out += codon_table[substr]

print(out)
