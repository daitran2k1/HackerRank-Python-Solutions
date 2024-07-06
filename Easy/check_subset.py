if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        na = int(input())
        sa = set(map(int, input().split()))
        nb = int(input())
        sb = set(map(int, input().split()))
        # # use difference
        # if len(sa - sb):
        #     print("False")
        # else:
        #     print("True")
        # use issubset
        print(sa.issubset(sb))
