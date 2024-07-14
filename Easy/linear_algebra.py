import numpy as np

if __name__ == "__main__":
    N = int(input())
    arr = np.array([input().split() for _ in range(N)], float)
    print(np.round(np.linalg.det(arr), 2))
