if __name__ == "__main__":
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))
    # # using union, intersection and difference operators
    # symmetric_difference = sorted(a.union(b).difference(a.intersection(b)))
    # # short cut
    symmetric_difference = sorted(a.symmetric_difference(b))
    for element in symmetric_difference:
        print(element)
