import numpy as np

if __name__ == "__main__":
    N, M, P = map(int, input().split())
    arr1 = np.array([input().split() for _ in range(N)], int)
    arr2 = np.array([input().split() for _ in range(M)], int)
    print(np.concatenate((arr1, arr2)))
