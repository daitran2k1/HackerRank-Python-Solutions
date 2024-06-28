if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    lowest_score = float("inf")
    second_lowest_score = float("inf")
    for name, grade in records:
        if grade < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = grade
        elif lowest_score < grade < second_lowest_score:
            second_lowest_score = grade

    second_lowest_students = sorted(
        [name for name, grade in records if grade == second_lowest_score]
    )
    for student in second_lowest_students:
        print(student)
