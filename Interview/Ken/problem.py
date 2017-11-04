my_map = [
'1112',
'1912',
'1892',
'1234']

def is_cavity (row, col, mapa):
    depth = mapa[row][col]
    return mapa[row-1][col] < depth and mapa[row][col-1] < depth and mapa[row][col+1] < depth and mapa[row+1][col] < depth

def change (row, col, map):
    new_row = list(map[row])
    new_row[col] = 'X'
    new_row = ''.join(new_row)
    map[row] = new_row


for y in range(1, len(my_map)-1):
    for x in range(1, len(my_map[0])-1):
        if is_cavity(y, x, my_map):
            change (y, x, my_map)


print(my_map)
