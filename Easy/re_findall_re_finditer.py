import re

if __name__ == "__main__":
    s = input()
    pattern = "(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
    matches = re.findall(pattern, s)
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)
