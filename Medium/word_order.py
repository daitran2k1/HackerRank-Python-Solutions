from collections import OrderedDict

if __name__ == "__main__":
    d = OrderedDict()
    n = int(input())
    for _ in range(n):
        s = input()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

    print(len(d))
    print(*d.values())
