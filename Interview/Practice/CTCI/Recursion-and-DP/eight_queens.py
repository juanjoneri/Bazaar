def backtracker(options, safe_up_to, size):
    solution = [None] * size

    def extend_solution(position):
        for option in options:
            solution[position] = option
            if safe_up_to(solution, position):
                if position == size-1 or extend_solution(position+1):
                    return solution

    return extend_solution(0)

def eight_queens(n):
    def valid(solution, upto):
        for col in range(upto):
            if (
                    solution[col] == solution[upto]                   # same row
                    or solution[col] == solution[upto] + upto - col   # diagonal
                    or solution[col] == solution[upto] + col - upto): # diagonal
                return False
        return True


    return backtracker(range(n), valid, n)

def main():
    print(eight_queens(4))


if __name__ == '__main__':
    main()
