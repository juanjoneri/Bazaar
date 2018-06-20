"""
You have an integer matrix representing a plot of land, where the values at that
location represents the height above the sea level. Avalue of zero indicates water.
A pond is a region of water connected horizontally, or diagonally. The size is
the number of connected water cells. Find the sizes of all ponds.
"""

class Map():
    def __init__(self, land):
        self.land = land
        self.nb_rows = len(land)
        self.nb_cols = len(land[0])
        self.visited = set()

    def neighbors_of(self, row, col):
        delta = [-1, 0, 1]
        for delta_row in delta:
            for delta_col in delta:
                n_row, n_col = row + delta_row, col + delta_col
                if 0 <= n_row < self.nb_rows and 0 <= n_col < self.nb_cols:
                    yield n_row, n_col

    def cluster_size(self, row, col):
        size = 1
        symbol = self.land[row][col]
        self.visited.add((row, col))

        for n_row, n_col in self.neighbors_of(row, col):
            if self.land[n_row][n_col] == symbol and (n_row, n_col) not in self.visited:
                size += self.cluster_size(n_row, n_col)

        return size

    def all_clusters(self, symbol):
        for row_i in range(self.nb_rows):
            for col_i in range(self.nb_cols):
                if self.land[row_i][col_i] == symbol and (row_i, col_i) not in self.visited:
                    yield self.cluster_size(row_i, col_i)


def pond_sizes(land, symbol=0):
    map_ = Map(land)
    print(list(map_.all_clusters(symbol)))


def main():
    LAND = [[0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]]


    pond_sizes(LAND)

if __name__ == '__main__':
    main()
