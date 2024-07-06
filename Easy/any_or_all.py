if __name__ == "__main__":
    # 3 lines of code or less challenge
    N = int(input())
    numbers = input().split()
    print(all([int(x) > 0 for x in numbers]) and any([x == x[::-1] for x in numbers]))
