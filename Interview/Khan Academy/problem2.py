hole_count = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}

sample = 9876

def solve(num):
    num_name = str(num)
    tot_holes = 0
    for number in num_name:
        tot_holes += hole_count[number]

    return tot_holes

print(solve(sample))
