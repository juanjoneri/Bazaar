
def merge(l, r):
    ans = []
    len_l, len_r = len(l), len(r)
    i_l = i_r = 0
   
    while len(ans) < (len_l + len_r):
        if i_l < len_l and i_r < len_r:
            if l[i_l] < r[i_r]:
                ans += [l[i_l]]
                i_l += 1
            else:
                ans += [r[i_r]]
                i_r += 1
        else:
            if i_l < len_l:
                ans += [l[i_l]]
                i_l += 1
            else:
                ans += [r[i_r]]
                i_r += 1

    return ans

def sort(l):
    m = len(l) // 2
    return l if len(l) <= 1 else merge(sort(l[:m]), sort(l[m:]))
    

if __name__ == '__main__':
    a = [1, 2, 4, 3, 4, 1, 0, 6, 11, 4]
    assert(sort(a) == [0, 1, 1, 2, 3, 4, 4, 4, 6, 11])
