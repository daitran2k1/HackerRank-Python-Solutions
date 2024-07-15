from collections import Counter

if __name__ == "__main__":
    c = Counter(sorted(input()))
    for char, count in c.most_common(3):
        print(char, count)
