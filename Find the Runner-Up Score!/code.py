n = int(input())
A = input()
A = A.split()
scores = []

for i in A:
    scores.append(int(i))

scores.sort()

how_many = scores.count(scores[n-1])
for x in range(how_many):
    scores.pop()

print(scores[n - how_many - 1])
