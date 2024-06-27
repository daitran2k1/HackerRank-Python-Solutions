if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = set(record[1] for record in records)
    lowest_score = min(scores)
    second_lowest_score = max(scores)
    for score in scores:
        if lowest_score < score < second_lowest_score:
            second_lowest_score = score

    people = sorted(
        [record[0] for record in records if record[1] == second_lowest_score]
    )
    for person in people:
        print(person)
