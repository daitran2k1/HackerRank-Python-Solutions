from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    s = sorted(s)
    k = int(k)
    for length in range(1, k + 1):
        for com in combinations(s, length):
            print("".join(com))
