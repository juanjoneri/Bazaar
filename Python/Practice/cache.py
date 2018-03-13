from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    print(fib(300))

if __name__ == '__main__':
    main()