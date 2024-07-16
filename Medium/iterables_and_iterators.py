from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    arr = input().split()
    K = int(input())
    all_combinations = list(combinations(arr, K))
    count = sum(1 for comb in all_combinations if "a" in comb)
    print(f"{count / len(all_combinations):.3f}")
