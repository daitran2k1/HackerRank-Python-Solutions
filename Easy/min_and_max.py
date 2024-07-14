import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = np.array([input().split() for _ in range(N)], int)
    min_arr = np.min(arr, axis=1)
    print(np.max(min_arr))
