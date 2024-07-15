from collections import deque
from typing import Deque


def check_valid(queue: Deque[int]):
    max_value = float("inf")
    while queue:
        if queue[0] >= queue[-1]:
            pick = queue.popleft()
        else:
            pick = queue.pop()

        if pick > max_value:
            return False

        max_value = pick

    return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        queue = deque(map(int, input().split()))
        if check_valid(queue):
            print("Yes")
        else:
            print("No")
