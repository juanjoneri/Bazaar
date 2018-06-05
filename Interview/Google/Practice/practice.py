# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def chunks(S, K):
    for i in range(math.ceil(len(S)/K)):
        start = i*K
        end = min((i+1)*K, len(S))
        yield S[start:end]

def solution2(S, K):
    reversed_clean = S.replace('-', '')[::-1].upper()
    answer = reversed([chunk[::-1] for chunk in chunks(reversed_clean, K)])
    return '-'.join(answer)


import re

def solution1(S, T):
    # write your code in Python 3.6
    pattern = '.*' + '.*'.join(list(T)) + '.*'
    regex = re.compile(pattern)
    return 1 if regex.match(S) else 0



def max_damage1(total_money, costs, damages, n):

    if n == 0 or total_money == 0 :
        return 0
    elif total_money < costs[n-1]:
        # not possible to use this last card
        return max_damage(total_money, costs, damages, n-1)


    including_last = max_damage(total_money - costs[n-1] , costs, damages, n-1) + costs[n-1]
    excluding_last = max_damage(total_money, costs, damages, n-1)

    return max(including_last, excluding_last)

def max_damage_with_memo(total_money, costs, damages, n=None, memo=dict()):
    if n == None:
        # default value of n
        n = len(costs)
    if n == 0 or total_money == 0 :
        # base case
        memo[(n, total_money)] = 0
    elif total_money < costs[n-1]:
        # not possible to use this last card
        memo[(n, total_money)] = max_damage_with_memo(total_money, costs, damages, n-1, memo)
    else:
        # recurse to find the best solution
        including_last = max_damage_with_memo(total_money - costs[n-1] , costs, damages, n-1, memo) + damages[n-1]
        excluding_last = max_damage_with_memo(total_money, costs, damages, n-1, memo)
        memo[(n, total_money)] = max(including_last, excluding_last)

    return memo[(n, total_money)]


def solution(total_money, total_damage, costs, damages):
    # write your code in Python 3.6
    max_damage = max_damage_with_memo(total_money, costs, damages)
    print(max_damage)
    return max_damage_with_memo(total_money, costs, damages) >= total_damage

if __name__ == '__main__':
    (total_money, total_damage, costs, damages) = (100, 12, [50, 60, 10, 5], [6, 4, 2, 1])
    """
    W -> total capacity
    wt -> weights
    val -> values
    n -> len(W)
    """
    print(solution(total_money, total_damage, costs, damages))
