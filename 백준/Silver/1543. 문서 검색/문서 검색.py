import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

print(doc.count(word))