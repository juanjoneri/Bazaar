"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""


from collections import defaultdict

def run_stairs(n, memo={0:1}):
    if n < 0:
        return 0
    if n not in memo:
        memo[n] = run_stairs(n-1) + run_stairs(n-2) + run_stairs(n-3)
    return memo[n]



def main():
    assert run_stairs(3) == 4
    assert run_stairs(1) == 1
    assert run_stairs(2) == 2


if __name__ == '__main__':
    main()
