if __name__ == "__main__":
    n = int(input())
    set1 = set(map(int, input().split()))
    b = int(input())
    set2 = set(map(int, input().split()))
    print(len(set1 & set2))
