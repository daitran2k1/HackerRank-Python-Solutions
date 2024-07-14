import numpy as np

np.set_printoptions(legacy="1.13")

if __name__ == "__main__":
    arr = np.array(input().split(), float)
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))
