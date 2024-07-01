import re

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input()
        try:
            re.compile(s)
            print(True)
        except re.error:
            print(False)
