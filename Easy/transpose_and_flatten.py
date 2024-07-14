import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = np.array([input().split() for _ in range(N)], int)
    print(np.transpose(arr))
    print(arr.flatten())
