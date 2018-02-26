# Find how many ways to arrange the students into teams, so that each team's skills summ up to a target value k

from sys import stdin

def combinations(values, n):
    if n == 0:
        yield []
    else:
        for i in range(len(values)):
            for combination in combinations(values[i+1:], n-1):
                yield [values[i]] + combination

def filter_combinations(combinations, k):
    return list(filter(lambda x: sum(x) == k, combinations))

if __name__ == '__main__':
    n = int(stdin.readline()) # numbr of students
    skills = list(map(int, stdin.readline().split())) # skill of each student
    k = int(stdin.readline()) # target skill of each team


    combinations_summing_k = filter_combinations(list(combinations(skills , 3)), k)
    print (len(combinations_summing_k))
