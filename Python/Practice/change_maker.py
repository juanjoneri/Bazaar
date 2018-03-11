from copy import deepcopy

def change_maker(coins):
    n = len(coins)

    # helper function for choosing which solution uses the least coins
    def least_coins(up, left):
        if all([up, left]):
            return left if sum(left) <= sum(up) else up
        elif any([up, left]):
            return left if left != None else up
        else:
            return None

    # dictionary from (change_left, coin_index) -> [best_change]
    # base case, 0 of each coin make 0 value
    best_change = {(0, i): [0]*n for i in range(n)}

    def make_change(value, coin_index=n-1):
        nonlocal best_change, coins
        if (value, coin_index) not in best_change:
            # Find best solution without the use of coin at coin_index...
            up = make_change(value, coin_index-1) if coin_index > 0 else None
            # Find best solution forcing the use of coin at coin_index
            left = make_change(value - coins[coin_index], coin_index) if value >= coins[coin_index] else None
            if left: left[coin_index] += 1
            
            # Choose the one that uses the least ammount of coins
            best_change[(value, coin_index)] = least_coins(up, left)
        
        return deepcopy(best_change[(value, coin_index)])

    # this function retains the state of best_change with all calculated solutions for constant time lookup as a hidden field!
    return make_change


if __name__ == '__main__':

    us = [2, 3, 9]
    us_change = change_maker(us)
    
    assert(us_change(0) == [0, 0, 0])
    assert(us_change(1) == None)
    assert(us_change(3) == [0, 1, 0])
    assert(us_change(9) == [0, 0, 1])
    assert(us_change(11) == [1, 0, 1]) 
    assert(us_change(12) == [0, 1, 1])
    print('us test passed')

    uru = [1, 2, 5, 10, 50]
    uru_change = change_maker(uru)
    assert(uru_change(0) == [0, 0, 0, 0, 0])
    assert(uru_change(3) == [1, 1, 0, 0, 0])
    assert(uru_change(-1) == None)
    assert(uru_change(99) == [0, 2, 1, 4, 1])
    print('uru tests passed')