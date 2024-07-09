import re

if __name__ == "__main__":
    s = input()
    k = input()
    matches = list(re.finditer(f"(?={k})", s))
    if matches:
        for match in matches:
            print((match.start(), match.start() + len(k) - 1))
    else:
        print((-1, -1))
