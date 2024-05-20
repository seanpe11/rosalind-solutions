s = input()
t = input()

pos = []
for x in range(0,len(s)-len(t)):
    if (s[x:x+len(t)] == t):
        print(x+1, end=' ')
