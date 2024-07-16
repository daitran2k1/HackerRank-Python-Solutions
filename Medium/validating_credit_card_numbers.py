import re

if __name__ == "__main__":
    N = int(input())
    pattern = r"^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$"
    for _ in range(N):
        s = input()
        if re.match(pattern, s):
            print("Valid")
        else:
            print("Invalid")
