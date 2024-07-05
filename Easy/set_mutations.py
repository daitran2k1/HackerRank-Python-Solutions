if __name__ == "__main__":
    n1 = int(input())
    s1 = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        operation, n2 = input().split()
        s2 = set(map(int, input().split()))
        match operation:
            case "intersection_update":
                s1 &= s2
            case "update":
                s1 |= s2
            case "symmetric_difference_update":
                s1 ^= s2
            case "difference_update":
                s1 -= s2

    print(sum(s1))
