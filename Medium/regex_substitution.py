import re

if __name__ == "__main__":
    N = int(input())
    text = "\n".join(input() for _ in range(N))
    text = re.sub(r"(?<= )&&(?= )", "and", text)
    text = re.sub(r"(?<= )\|\|(?= )", "or", text)

    print(text)
