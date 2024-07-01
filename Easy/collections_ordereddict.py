from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    net_prices = OrderedDict()
    for _ in range(N):
        *item, price = input().split()
        item = " ".join(item)
        price = int(price)
        if item in net_prices:
            net_prices[item] += price
        else:
            net_prices[item] = price

    for item, price in net_prices.items():
        print(item, price)
