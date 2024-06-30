from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    columns = input().split()
    Student = namedtuple("Student", columns)
    students = [Student(*input().split()) for _ in range(N)]
    average = sum(int(student.MARKS) for student in students) / N
    print(f"{average:.2f}")

# # 4 lines of code or less challenge
# from collections import namedtuple
# N = int(input())
# Student = namedtuple("Student", input().split())
# print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(N)) / N:.2f}")
