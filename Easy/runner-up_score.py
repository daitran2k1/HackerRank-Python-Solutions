if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    best_score = float("-inf")
    runner_up_score = float("-inf")
    for score in arr:
        if score > best_score:
            runner_up_score = best_score
            best_score = score
        elif best_score > score > runner_up_score:
            runner_up_score = score

    print(runner_up_score)
