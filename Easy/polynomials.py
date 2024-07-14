import numpy as np

if __name__ == "__main__":
    coefficients = np.array(input().split(), float)
    print(np.polyval(coefficients, float(input())))
