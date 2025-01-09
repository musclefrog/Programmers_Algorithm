X = int(input())
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

sum = 0
for price, quantity in arr:
    sum += price * quantity
if sum == X:
    print("Yes")
else:
    print("No")