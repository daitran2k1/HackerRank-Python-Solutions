if __name__ == "__main__":
    N, M = map(int, input().split())
    symbol = ".|."
    for i in range(N // 2):
        print((symbol * (i * 2 + 1)).center(M, "-"))

    print(("WELCOME").center(M, "-"))
    for i in reversed(range(N // 2)):
        print((symbol * (i * 2 + 1)).center(M, "-"))
