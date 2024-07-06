import re

if __name__ == "__main__":
    T = int(input())
    pattern = "^[-+]?\d*\.\d+$"
    for _ in range(T):
        N = input()
        if re.match(pattern, N):
            try:
                float(N)
                print("True")
            except ValueError:
                print("False")
        else:
            print("False")
