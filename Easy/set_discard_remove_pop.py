if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        match input().split():
            case ["pop"]:
                s.pop()
            case ["discard", val]:
                s.discard(int(val))
            case ["remove", val]:
                s.remove(int(val))

    print(sum(s))
