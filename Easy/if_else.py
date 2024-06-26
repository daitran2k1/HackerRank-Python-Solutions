if __name__ == "__main__":
    n = int(input().strip())
    if n % 2:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif n <= 20:
        print("Weird")
    else:
        print("Not Weird")
