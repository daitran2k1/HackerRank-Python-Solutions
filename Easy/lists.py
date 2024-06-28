if __name__ == "__main__":
    arr = []
    N = int(input())
    for _ in range(N):
        match input().split():
            case ["insert", int(i), int(e)]:
                arr.insert(i, e)
            case ["print"]:
                print(arr)
            case ["remove", e]:
                arr.remove(int(e))
            case ["append", e]:
                arr.append(int(e))
            case ["sort"]:
                arr.sort()
            case ["pop"]:
                arr.pop()
            case ["reverse"]:
                arr.reverse()
