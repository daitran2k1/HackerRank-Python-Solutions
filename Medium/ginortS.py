def custom_sort_key(char):
    if char.islower():
        return (0, char)

    if char.isupper():
        return (1, char)

    if char.isdigit():
        if int(char) % 2:
            return (2, char)

        return (3, char)


if __name__ == "__main__":
    S = input()
    print("".join(sorted(S, key=custom_sort_key)))
