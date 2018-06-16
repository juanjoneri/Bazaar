"""
Given a dictionary of names, find if a given name can be smashed into a single
character by reducing the name one character at the time, and where all intermediate
names are also in the dictionary

'SPRINT' -> 'PRINT' -> 'PINT' -> 'PIT' -> 'IT' -> 'I'
"""




class Word():
    def __init__(self, name, dictionary):
        if name not in dictionary:
            raise AttributeError(f'word: {name} is not in dictionary')

        self.dictionary = dictionary
        self.name = name
        self.children = []

        for i in range(len(name)):
            child_name = name[:i]+name[i+1:]
            if child_name in dictionary:
                self.children.append(Word(child_name, dictionary))

    def __repr__(self):
        return f'{self.name} -> ({repr(self.children)})'

    @property
    def collapsable(self):
        if len(self.name) == 1:
            return True

        for child in self.children:
            if child.collapsable:
                return True

        # print(self.name)
        return False


def main():
    dictionary = {"A", "AFRICA", "AN", "LANE", "PAN", "PANT", "PLANET", "PLANT"}

    assert not Word('AFRICA', dictionary).collapsable
    assert Word('PLANET', dictionary).collapsable

    assert not Word('LANE', dictionary).collapsable
    assert Word('PANT', dictionary).collapsable

if __name__ == '__main__':
    main()
