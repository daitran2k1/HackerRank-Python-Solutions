if __name__ == "__main__":
    N, X = map(int, input().split())
    all_subject_marks = []
    for _ in range(X):
        subject_marks = map(float, input().split())
        all_subject_marks.append(subject_marks)

    for student_marks in zip(*all_subject_marks):
        average = sum(student_marks) / X
        print(f"{average:.1f}")
