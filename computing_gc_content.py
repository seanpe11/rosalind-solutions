# https://rosalind.info/problems/gc/

filename = input()
fo = open(filename, "r")

ids = []
counts = []
cur = 0
curCount = 0

ids.append(fo.readline()[1:-1])
for line in fo:
    if (line[0] == '>'):
        counts.append(cur / curCount)
        ids.append(line[1:-1])
        cur = 0
        curCount = 0
    else:
        for x in line:
            if (x == 'C' or x == 'G'):
                cur+=1
                curCount+=1
            elif (x == 'A' or x == 'T'):
                curCount+=1


cur = 0
curCount = 0
for x in line:
    if (x == 'C' or x == 'G'):
        cur+=1
        curCount+=1
    elif (x == 'A' or x == 'T'):
        curCount+=1
counts.append(cur / curCount)

# print(counts)
# print(ids)
print(ids[counts.index(max(counts))])
print(f"{max(counts) * 100:.6f}")
