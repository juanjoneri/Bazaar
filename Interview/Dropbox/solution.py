import sys

class Folder:
    def __init__(self, id, contents=[], confidential=False):
        self.id = id
        self.contents = set(contents)
        self.confidential = confidential
        self.subfolders = set()

    @property
    def is_leaf(self):
        return not any(self.subfolders)

    def add_contents(self, new_contents):
        self.contents.update(new_contents)

    def add_subfolder(self, other):
        self.subfolders.add(other)
        if not other.confidential:
            other.add_contents(self.contents)


if __name__ == '__main__':

    input_file = sys.stdin
    total_lines = int(input_file.readline())

    # Build Folders and Cows

    all_folders = dict()
    all_cows = set()
    shared_lines, confidential_lines = map(int, input_file.readline().split())

    for current_line in range(shared_lines + confidential_lines):
        folder_id, *folder_contents = map(int, input_file.readline().split())
        is_confidential = current_line >= shared_lines
        new_folder = Folder(folder_id, folder_contents, is_confidential)
        all_folders[folder_id] = (new_folder)
        all_cows.update(folder_contents)

    # Extablish Folder herarchy

    ralationship_lines = int(input_file.readline())

    for current_line in range(ralationship_lines):
        parent, child = map(int, input_file.readline().split())
        all_folders[parent].add_subfolder(all_folders[child])

    # Find uncool cows

    uncool_cows = set()

    for folder_id, folder in all_folders.items():
        if folder.is_leaf and folder.confidential:
            uncool_cows.update(all_cows - folder.contents)

    print(*sorted(uncool_cows), sep=' ')
