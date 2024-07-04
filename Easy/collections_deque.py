from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()
    for _ in range(N):
        match input().split():
            case ["append", val]:
                d.append(int(val))
            case ["pop"]:
                d.pop()
            case ["popleft"]:
                d.popleft()
            case ["appendleft", val]:
                d.appendleft(int(val))

    print(*d)
