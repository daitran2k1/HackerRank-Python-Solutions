import re

if __name__ == "__main__":
    pattern = r"^[789]\d{9}$"
    N = int(input())
    for _ in range(N):
        s = input().strip()
        if re.match(pattern, s):
            print("YES")
        else:
            print("NO")
