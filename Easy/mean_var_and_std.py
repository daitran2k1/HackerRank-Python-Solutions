import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = np.array([input().split() for _ in range(N)], int)
    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(np.round(np.std(arr), 11))
