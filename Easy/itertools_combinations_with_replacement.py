from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, k = input().split()
    s = sorted(s)
    k = int(k)
    for combination in combinations_with_replacement(s, k):
        print("".join(combination))
