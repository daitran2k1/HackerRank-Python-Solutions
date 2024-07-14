import numpy as np

if __name__ == "__main__":
    arrA = np.array(input().split(), int)
    arrB = np.array(input().split(), int)
    print(np.inner(arrA, arrB))
    print(np.outer(arrA, arrB))
