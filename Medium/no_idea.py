if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    happiness = 0
    for ele in arr:
        if ele in A:
            if ele not in B:
                happiness += 1
        elif ele in B:
            happiness -= 1

    print(happiness)
