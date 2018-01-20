import sys

class Folder:
    def __init__(self, id, members=[], confidential=False):
        self.id = id
        self.members = set(members)
        self.confidential = confidential
        self.subfolders = set()

    @property
    def is_leaf(self):
        return not any(self.subfolders)

    def add_members(self, new_members):
        self.members.update(new_members)

    def add_subfolder(self, other):
        self.subfolders.add(other)
        if not other.confidential:
            other.add_members(self.members)


if __name__ == '__main__':

    input_file = sys.stdin
    total_lines = int(input_file.readline())

    # Build Folders and Cows

    all_folders = dict()
    all_cows = set()
    shared_lines, confidential_lines = map(int, input_file.readline().split())

    for current_line in range(shared_lines + confidential_lines):
        folder_id, *folder_members = map(int, input_file.readline().split())
        is_confidential = current_line >= shared_lines
        new_folder = Folder(folder_id, folder_members, is_confidential)
        all_folders[folder_id] = (new_folder)
        all_cows.update(folder_members)

    # Extablish Folder herarchy

    ralationship_lines = int(input_file.readline())

    for current_line in range(ralationship_lines):
        parent, child = map(int, input_file.readline().split())
        all_folders[parent].add_subfolder(all_folders[child])

    # Find uncool Cows

    uncool_cows = set()
    for folder in all_folders.itervalues():
        if folder.is_leaf and folder.confidential:
            uncool_cows.update(all_cows - folder.members)

    print(*sorted(uncool_cows), sep=' ')
