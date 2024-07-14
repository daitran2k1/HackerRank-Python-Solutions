import numpy as np

if __name__ == "__main__":
    sizes = list(map(int, input().split()))
    print(np.zeros(sizes, int))
    print(np.ones(sizes, int))
