q(int)\n
m(number of shared lines) n(number of confidencial lines)\n

-folderID(int) [folderMembers(int) cows]
-folderID(int) [folderMembers(int) cows]
-...

g(number of lines)\n
-u(int, parent folderID) v(int, child folderID)
-u(int, parent folderID) v(int, child folderID)
-...



----------------------
- folders have cows (numbers)
- folders are shared or confidential
- keep track of cows in set and put in folder
- keep track of cows globally
- save folders in hashmap by folderID

- once folders are created stablish relationships between them
- access from hashmap by folderID
- if child is shared -> add parents folders to child (inherits its parents contents)

- iterate over all leaf folders (with no children)
- find all cows that can't access this leaf folder
- save as uncool cows

- output sorted uncool cows separated by " "
