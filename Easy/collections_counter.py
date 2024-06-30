from collections import Counter

if __name__ == "__main__":
    num_shoes = int(input())
    shoe_sizes = map(int, input().split())
    num_customers = int(input())
    shop = Counter(shoe_sizes)
    revenue = 0
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if shop[size]:
            shop[size] -= 1
            revenue += price

    print(revenue)
