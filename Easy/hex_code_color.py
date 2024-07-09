import re

if __name__ == "__main__":
    pattern = r"#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?\b(?!\s*{)"
    N = int(input())
    css_code = [input().strip() for _ in range(N)]
    css_code = " ".join(css_code)
    for match in re.findall(pattern, css_code):
        print(match)
