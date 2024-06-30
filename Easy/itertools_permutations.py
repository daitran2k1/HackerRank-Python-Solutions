from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()
    s = sorted(s)
    k = int(k)
    for sample in permutations(s, k):
        print("".join(sample))
