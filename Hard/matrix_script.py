import re

N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
string = "".join(matrix[i][j] for j in range(M) for i in range(N))
string = re.sub(r"(?<=[a-zA-Z0-9])([!@#$%& ]+)(?=[a-zA-Z0-9])", " ", string)
print(string)
