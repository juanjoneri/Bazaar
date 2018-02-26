# Find how many ways to arrange the students into teams, so that each team's skills summ up to a target value k

from sys import stdin
from collections import Counter
from math import factorial

def nck(n, k):
    # n choose k: arangements of k elements from a set of n
    return factorial(n) // (factorial(k) * factorial(n-k))

if __name__ == '__main__':
    n = int(stdin.readline()) # numbr of students
    skills = list(map(int, stdin.readline().split())) # skill of each student
    skills_counts = Counter(skills) # how many students have a certain skill
    k = int(stdin.readline()) # target skill of each team

    possible_skills = list(filter(lambda x: 0 <= x <= k, skills))
    possible_n = len(possible_skills)

    unique_skills = list(set(possible_skills))
    unique_n = len(unique_skills)

    repeated_skills = list(filter(lambda x: skills_counts[x] >= 2, possible_skills))

    # find all unique pairs of sutudents'skills
    skills_pairs = dict() # n^2
    for i in range(unique_n):
        for j in range(i+1, unique_n):
            pair = tuple(sorted((unique_skills[i], unique_skills[j])))
            skill = sum(pair)
            if skill not in skills_pairs:
                skills_pairs[skill] = [pair]
            elif pair not in skills_pairs[skill]:
                skills_pairs[skill].append(pair)

    for skill in repeated_skills:
        pair = (skill, skill)
        skill = 2*skill
        if skill not in skills_pairs:
            skills_pairs[skill] = [pair]
        elif pair not in skills_pairs[skill]:
            skills_pairs[skill].append(pair)

    # find all unique trios of students's skills that add up to k
    skills_trios = set()
    for skill in unique_skills:
        target_skill = k - skill
        if target_skill in skills_pairs:
            for pair in skills_pairs[target_skill]:
                # check if we will not repeat a student in this trio
                if skills_counts[skill] > pair.count(skill):
                    trio = tuple(sorted((skill, *pair)))
                    skills_trios.add(trio)

    count = 0
    for x, y, z in skills_trios:
        # find how many ways this trio could have been formed
        if x == y == z:
            count += nck(skills_counts[x], 3)
        elif x == y:
            count += (nck(skills_counts[x], 2) * skills_counts[z])
        elif y == z:
            count += (skills_counts[x] * nck(skills_counts[y], 2))
        elif x == z:
            count += (nck(skills_counts[x], 2) * skills_counts[y])
        else:
            count += (skills_counts[x] * skills_counts[y] * skills_counts[z])


    print(count)
