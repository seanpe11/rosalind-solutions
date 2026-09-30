n, m = [int(z) for z in input().split()]
### 1, 1,

arr = []


def recurrent_rabbits(n, m, total, mature, young) -> int:
    young = mature + young
    total = mature + young
    if n == 0:
        return total
