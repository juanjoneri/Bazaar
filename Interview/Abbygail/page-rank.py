import math
from collections import deque

class SearchItem(object):

    def __init__(self, host_ID, listing_ID, score, city):
        self.host_ID = int(host_ID)
        self.listing_ID = int(listing_ID)
        self.score = float(score)
        self.city = city

    def __str__(self):
        # for printing results
        return '{},{},{},{}'.format(self.host_ID, self.listing_ID, self.score, self.city)

    def __eq__(self, other):
        # for checking if in page
        return self.host_ID == other.host_ID

def uniques(list1, list2):
    # returns the index of the next element from list2 that is not in list1
    for i in range(len(list2)):
        if list2[i] not in list1:
            yield i

def paginate(num, results):
    items = [SearchItem(*result.split(',')) for result in results] # assuming input has correct format

    leftovers = deque() # used as a queue
    pages = [[] for _ in range(math.ceil(len(results) / num))]  # 2D list representing pages

    while any(items) or any(leftovers):
        current_item = leftovers.popleft() if any(leftovers) else items.pop(0) # try to follow score order
        current_page = next(page for page in pages if len(page) < num)

        if current_item not in current_page:
            current_page.append(current_item)
        else:
            try:
                next_unique_index = next(uniques(current_page, items))
                current_page.append(items.pop(next_unique_index))
            except StopIteration:
                if any(leftovers):
                    current_page.append(leftovers.popleft())
                else:
                    current_page.append(current_item)
                    continue
            leftovers.append(current_item)

    paginated_results = []
    separator = ''
    for page in pages:
        paginated_results.extend(map(str, page))
        paginated_results.append(separator)
    paginated_results.pop() # there is an extra separator

    return paginated_results

if __name__ == '__main__':
    results = [
    "1,28,300.6,San Francisco",
    "2,5,209.1,San Francisco",
    "1,10,205,San Francisco",
    "3,7,203.4,Oakland",
    "4,8,202.9,San Francisco",
    "1,10,199.8,San Francisco",
    "5,16,190.5,San Francisco",
    "1,10,190,San Francisco",
    ]
    num = 3
    print(paginate(num, results))
