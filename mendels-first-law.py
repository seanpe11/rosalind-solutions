# https://rosalind.info/problems/iprb/
## you just need to find the number of nn, nm * .50, mn * .50 (don't forget that although combination is the same, selection is different) and multiply nm by 1/4


def solution(k, m, n):
    ans = 0
    total = k + m + n
    ans += (n / total) * (n - 1) / (total - 1)  # nn aa and aa on punnett
    ans += ((n / total) * (m) / (total - 1)) * 0.50  # nm Aa and aa on punnett
    ans += ((m / total) * (n) / (total - 1)) * 0.50  # nm Aa and aa on punnett
    ans += ((m / total) * (m - 1) / (total - 1)) * 0.25  # mm Aa and Aa on punnett
    print(ans)  # prob of recessive

    return 1 - ans


def main():
    k = 30
    k = 28
    m = 25

    ans = solution(k, m, n)

    print(ans)


if __name__ == "__main__":
    main()
