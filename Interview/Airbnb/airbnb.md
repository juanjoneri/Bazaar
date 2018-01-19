```python
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

    leftovers = [] # used as a queue
    pages = [[] for _ in range(len(results) // num + 1)] # 2D list representing pages

    while any(items):
        current_item = leftovers.pop(0) if any(leftovers) else items.pop(0) # try to follow score order
        current_page = next(page for page in pages if len(page) < num)

        if current_item not in current_page:
            current_page.append(current_item)
        else:
            try:
                next_unique_index = next(uniques(current_page, items))
                current_page.append(items.pop(next_unique_index))
            except StopIteration:
                if any(leftovers):
                    current_page.append(leftovers.pop(0))
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
    "4,5,209.1,San Francisco",
    "20,7,203.4,Oakland",
    "6,8,202.9,San Francisco",
    "6,10,199.8,San Francisco",
    "1,16,190.5,San Francisco",
    "6,29,185.3,San Francisco",
    "7,20,180.0,Oakland",
    "6,21,162.2,San Francisco",
    "2,18,161.7,San Jose",
    "2,30,149.8,San Jose",
    "3,76,146.7,San Francisco",
    "2,14,141.8,San Jose"
    ]
    num = 5
    print(paginate(num, results))

```

### Output

```
[
'1,28,300.6,San Francisco', 
'4,5,209.1,San Francisco', 
'20,7,203.4,Oakland', 
'6,8,202.9,San Francisco', 
'7,20,180.0,Oakland', 
'', 
'6,10,199.8,San Francisco', 
'1,16,190.5,San Francisco',
'2,18,161.7,San Jose', 
'3,76,146.7,San Francisco',
'6,29,185.3,San Francisco', 
'', 
'6,21,162.2,San Francisco', 
'2,30,149.8,San Jose',
'2,14,141.8,San Jose'
]

```

### Bugs

```python
#Problem
leftover q might have elements and conidtion any(itmes) will be false
#Fix
check if any(leftovers)
- while any(itmes)
+ while any(items) or any(leftovers):
# This fix will print the repetition last even when it has a higher ranking (this is ok)
6, results = [
    "1,28,300.6,San Francisco",
    "2,5,209.1,San Francisco",
    "3,7,203.4,Oakland",
    "4,8,202.9,San Francisco",
    "1,10,199.8,San Francisco",
    "5,16,190.5,San Francisco"
    ]

returns = [
    '1,28,300.6,San Francisco',
    '2,5,209.1,San Francisco',
    '3,7,203.4,Oakland', 
    '4,8,202.9,San Francisco',
    '5,16,190.5,San Francisco', 
    '']
```
```python
#Problem
Creating 1 more page than was needed when division is exact
#Fix:
+ import math
- pages = [[] for _ in range(len(results) // num + 1)]
+ pages = [[] for _ in range(math.ceil(len(results) / num))] 

1, results = [
    '1,28,300.6,San Francisco',
    '4,5,209.1,San Francisco',
    '20,7,203.4,Oakland',
    '6,8,202.9,San Francisco',
    '6,10,199.8,San Francisco'
    ]
returns = [
    '1,28,300.6,San Francisco', 
    '',
    '4,5,209.1,San Francisco',
    '',
    '20,7,203.4,Oakland', 
    '', 
    '6,8,202.9,San Francisco',
    '', 
    '6,10,199.8,San Francisco', 
    '']

6, results = [
    "1,28,300.6,San Francisco",
    "1,5,209.1,San Francisco",
    "1,7,203.4,Oakland",
    "1,8,202.9,San Francisco",
    "1,10,199.8,San Francisco",
    "1,16,190.5,San Francisco"
    ]
returns = [
    '1,28,300.6,San Francisco',
    '1,5,209.1,San Francisco',
    '1,7,203.4,Oakland', 
    '1,8,202.9,San Francisco',
    '1,10,199.8,San Francisco',
    '1,16,190.5,San Francisco',
    '']
```

### Comments

```python
#Maybe SearchItem object is overkill, use a closure like O'Reilly Cookbook's
def sample():
    n = 0
    # Closure function
    def func():
    	print('n=', n)
    
    # Accessor methods for n
    def get_n():
    	return n
    def set_n(value):
    	nonlocal n
   		n = value
    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func
if __name__ == '__main__'
    f = sample()
    f()          # n= 0
    f.set_n(10)
    f()          # n= 10
    f.get_n()    # 10
```

```python
# Find a better name for this function so you dont need a comment! although this name makes its usage very pretty: next(unique)
# I know! this should be a closure that takes one of the two list as a parameter and the other is stored: not_in_page = uniques(page); next(not_in_page(items))
def uniques(list1, list2):
    # returns the index of the next element from list2 that is not in list1
    for i in range(len(list2)):
        if list2[i] not in list1:
            yield i
```

```python
#The continue in line 44 seems like a patch. Maybe there is a cleaner way
```

