from itertools import product

if __name__ == "__main__":
    K, M = map(int, input().split())
    arrs = [list(map(int, input().split()))[1:] for _ in range(K)]
    max_value = 0
    for sample in product(*arrs):
        value = sum(x**2 for x in sample) % M
        max_value = max(max_value, value)

    print(max_value)
