import sys
import heapq

class SearchItem(object):

    def __init__(self, host_ID, list_ID, points, city):
        self.host_ID = int(host_ID)
        self.list_ID = int(list_ID)
        self.points = float(points)
        self.city = city

    def __str__(self):
        # for printing results
        return '{},{},{},{}'.format(self.host_ID, self.list_ID, self.points, self.city)

    def __lt__(self, other):
        # for ordering the heap
        if self.points == other.points:
            return 0
        return self.points < other.points

    def __eq__(self, other):
        # for checking if in page
        return self.host_ID == other.host_ID

def uniques(list1, list2):
    # returns the index of the next element from list2 that is not in list1
    for i in range(len(list2)):
        if list2[i] not in list1:
            yield i

if __name__ == '__main__':
    # Assuming first two lines represent capacity and the desired iterms to be proccesed
    capacity = int(sys.stdin.readline())
    items_count = int(sys.stdin.readline())

    items = []
    # could iterate over the stdin iterable but migh parse more than desirable items (items_count)
    for _ in range(items_count):
        try:
            line = sys.stdin.readline().rstrip('\n').split(',')
            new_item = SearchItem(*line)
            items.append(new_item)
        except TypeError:
            print('{} does not represent a search item'.format(line))
            exit()

    # Only process the required ammount of items
    pages = [[] for _ in range(items_count // capacity + 1)] # init empty 2D list
    leftovers = [] # max heap of items with used host_ID
    while any(items):
        current_item = heapq.heappop(leftovers) if any(leftovers) else items.pop(0) # try to follow impout order
        current_page = next(page for page in pages if len(page) < 5)

        if current_item not in current_page:
            current_page.append(current_item)
        else:
            try:
                next_unique_index = next(uniques(current_page, items))
                current_page.append(items.pop(next_unique_index))
            except StopIteration:
                if any(leftovers):
                    current_page.append(heapq.heappop(leftovers))
                else:
                    current_page.append(current_item)
                    continue
            heapq.heappush(leftovers, current_item)

    for page in pages:
        for item in page:
            print(item)
        print()
