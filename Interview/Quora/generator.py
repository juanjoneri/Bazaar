from random import randrange

n = 5000
print(n)

students = []
for _ in range(n):
    students.append(str(randrange(1, 50)))
print(" ".join(students))

k = randrange(150)
print(k)
