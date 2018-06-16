"""
Write an algorithm which computes teh number of trailing zeros in n factorial
"""



def facotor_counter(factor):
    '''counts the number of times that factor appears in the prime factorization of number'''
    def counter(number):
        count = 0
        while number % factor == 0:
            count += 1
            number /= factor
        return count

    return counter


def trailing_zeros(n):
    twos = fives = 0
    twos_counter, fives_counter = facotor_counter(2), facotor_counter(5)

    for i in range(1, n+1):
        twos += twos_counter(i)
        fives += fives_counter(i)

    return min(twos, fives)






def main():
    assert trailing_zeros(1) == 0
    assert trailing_zeros(5) == 1 # 120
    assert trailing_zeros(9) == 1 # 362880
    assert trailing_zeros(10) == 2 # 3628800
    assert trailing_zeros(123) == 28# ....4952960000000000000000000000000000

if __name__ == '__main__':
    main()
