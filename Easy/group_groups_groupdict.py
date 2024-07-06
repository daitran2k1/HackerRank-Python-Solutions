import re

if __name__ == "__main__":
    s = input()
    pattern = r"([a-zA-Z0-9])\1"
    match = re.search(pattern, s)
    print(match.group(1) if match else -1)
