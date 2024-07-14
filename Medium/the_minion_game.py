def minion_game(string: str):
    VOWELS = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in VOWELS:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if stuart_score == kevin_score:
        print("Draw")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print(f"Kevin {kevin_score}")


if __name__ == "__main__":
    s = input()
    minion_game(s)
