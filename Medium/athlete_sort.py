if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    sorted_arr = sorted(arr, key=lambda x: x[K])
    for ele in sorted_arr:
        print(*ele)
