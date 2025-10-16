x, y = map(int, input().split())

set1 = set([input().strip() for _ in range(x)])
set2 = set([input().strip() for _ in range(y)])

answer = list(set1 & set2)
answer.sort()

print(len(answer))
for man in answer:
    print(man)