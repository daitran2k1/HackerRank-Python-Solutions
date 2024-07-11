def wrapper(f):
    def fun(l):
        numbers = []
        for number in l:
            standardized_number = number[-10:]
            numbers.append(f"+91 {standardized_number[:5]} {standardized_number[5:]}")

        f(numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
