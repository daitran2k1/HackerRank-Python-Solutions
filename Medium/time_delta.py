from datetime import datetime


def time_delta(t1: str, t2: str):
    form = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, form)
    t2 = datetime.strptime(t2, form)
    return int(abs((t1 - t2).total_seconds()))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))
