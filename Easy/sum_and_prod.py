import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = np.array([input().split() for _ in range(N)], int)
    sum_arr = np.sum(arr, axis=0)
    print(np.prod(sum_arr))
