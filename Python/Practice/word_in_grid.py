

def backtracker(options, solves, size, start=[]):
    # solves is a so 'far so good' function for possible solution
    def extend(solution):
        for option in options:
            solution.append(option)
            if solves(solution):
                if len(solution) == size or extend(solution):
                    return solution
            solution.pop()
        return None

    return extend(start)

class Grid:
    def __init__(self, grid):
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid

    def contains(self, word):
        # returns a list of adjacent coordinates that form word
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == word[0]:
                    start = (row, col)
                    solution_starting = backtracker(self.options, lambda sol: self.matches(word, sol), len(word), [start])
                    if solution_starting:
                        return solution_starting
        
        return None

    def matches(self, name, coords):
        # coords: [(start), (delta1), (delta2) ...]
        row, col = coords[0]
        word = self.grid[row][col]
        used = {(row, col)}
        
        for d_row, d_col in coords[1:]:
            row += d_row
            col += d_col
            
            if (row, col) in used:
                return False
            else:
                used.add((row, col))
            
            if 0 <= row < self.height and 0 <= col < self.width:
                word += self.grid[row][col]
            else:
                return False
        
        return name.startswith(word)

    @property
    def options(self):
        delta = [1, -1, 0]
        self._options = set() 
        for d_row in delta:
            for d_col in delta:
                if d_row != d_col:
                    self._options.add((d_row, d_col))
        return self._options

if __name__ == '__main__':
    grid = [
        'ABCE',
        'SFCS',
        'ADEE'
    ]

    g = Grid(grid)
    assert(g.contains('ABCCED') != None)
    assert(g.contains('SEEDASFBA') != None)
    assert(g.contains('ABCB') == None)

    print('all tests passed')