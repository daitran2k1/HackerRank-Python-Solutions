import re


def is_valid(uid: str):
    if len(re.findall(r"[A-Z]", uid)) < 2:
        return False

    if len(re.findall(r"[0-9]", uid)) < 3:
        return False

    if not uid.isalnum():
        return False

    if len(set(uid)) != len(uid) or len(uid) != 10:
        return False

    return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        uid = input()
        if is_valid(uid):
            print("Valid")
        else:
            print("Invalid")
