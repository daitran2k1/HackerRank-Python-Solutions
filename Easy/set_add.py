if __name__ == "__main__":
    N = int(input())
    stamps = set()
    for _ in range(N):
        stamp = input().strip()
        stamps.add(stamp)

    print(len(stamps))
