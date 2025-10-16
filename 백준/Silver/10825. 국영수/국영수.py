import sys
input = sys.stdin.readline
n = int(input())
student = []
for i in range(n):
    chunk = input().split()
    student.append([chunk[0], int(chunk[1]), int(chunk[2]), int(chunk[3])])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for stu in student:
    print(stu[0])