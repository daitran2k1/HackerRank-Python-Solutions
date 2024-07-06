if __name__ == "__main__":
    set_A = set(map(int, input().split()))
    n = int(input())
    is_strict_superset = True
    for _ in range(n):
        set_B = set(map(int, input().split()))
        if not (set_A > set_B):
            is_strict_superset = False
            break

    print(is_strict_superset)
