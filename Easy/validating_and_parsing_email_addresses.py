import re

if __name__ == "__main__":
    pattern = r"^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    N = int(input())
    for _ in range(N):
        name, email = input().split()
        if re.match(pattern, email[1:-1]):
            print(name, email)
