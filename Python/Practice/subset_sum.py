
def subset_sum(values, sum, memo={}):
    if sum == 0:
        return [[]]
    elif not any(values):
        return [None]
    
    n = len(values)
    if (n, sum) not in memo:        
        last = values[-1]
        with_last = subset_sum(values[:-1], sum-last, memo)
        without_last = subset_sum(values[:-1], sum, memo)
        
        with_last = [[*conv, last] for conv in with_last if conv != None]
              
        memo[(n, sum)] = with_last + without_last
    
    return memo[(n, sum)]

def main():
    unique = {tuple(sorted(conv)) for conv in subset_sum([3, 4, 6, 3, 4, 3, 3, 6, 4], 12) if conv != None}
    print(unique)

if __name__ == '__main__':
    main()