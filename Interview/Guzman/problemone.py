def solution(A, B):
    if A in B:
        for i in range(len(B) // len(A) + 2):
            if B in A*i:
                return i
    return -1



if __name__ == '__main__':
    #Same usage of the app
    print(solution('abcd', 'cdabcdab'))
