import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr1 = np.array([input().split() for _ in range(N)], int)
    arr2 = np.array([input().split() for _ in range(N)], int)
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 * arr2)
    print(arr1 // arr2)
    print(arr1 % arr2)
    print(arr1**arr2)
