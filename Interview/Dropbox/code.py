from sys import stdin

class Folder:
    def __init__(self, id, members=[], confidential=False):
        self.id = id
        self.members = set(members)
        self.confidential = confidential
        self.subfolders = set()

    @property
    def is_leaf(self):
        return not any(self.subfolders)

    def inherit_members(self, new_members):
        self.members.update(new_members)

    def add_subfolder(self, other):
        self.subfolders.add(other)
        if not other.confidential:
            other.inherit_members(self.members)

if __name__ == '__main__':

    Q = int(stdin.readline()) # Number of cows

    ## Build Folders and Cows

    all_folders = dict()
    all_cows = set(range(Q))

    # M: number of shared folders
    # N: number of confidential folders
    M, N = map(int, stdin.readline().split())

    for current_line in range(M + N):
        folder_id, K, *folder_members = map(int, stdin.readline().split())
        is_confidential = current_line >= M
        new_folder = Folder(folder_id, folder_members, is_confidential)
        all_folders[folder_id] = new_folder

    ## Extablish Folder herarchy

    # G: Number of parent child relationships
    G = int(stdin.readline())

    for _ in range(G):
        # U: parent folder id
        # V: child folder id
        U, V = map(int, stdin.readline().split())
        all_folders[U].add_subfolder(all_folders[V])

    ## Find uncool Cows

    uncool_cows = set()

    for folder in all_folders.values():
        if folder.is_leaf:
            # all cows that cannot access this folder are uncool!
            uncool_cows.update(all_cows - folder.members)

    ## Format and output result to stdout

    print(*sorted(uncool_cows), sep=' ')
