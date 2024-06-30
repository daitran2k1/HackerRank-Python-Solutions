def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
