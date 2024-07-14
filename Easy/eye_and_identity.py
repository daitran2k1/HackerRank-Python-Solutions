import numpy as np

np.set_printoptions(legacy="1.13")

if __name__ == "__main__":
    N, M = map(int, input().split())
    print(np.eye(N, M))
