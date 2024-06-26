if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    best_score = max(arr)
    runner_up_score = -101
    for score in arr:
        if score < best_score and score > runner_up_score:
            runner_up_score = score

    print(runner_up_score)
