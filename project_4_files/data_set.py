"""
Oliver Rothe

data set representing hops to finish line by frog. 
demonstration of both linear and binary search algorithms
"""

#data set
hops = [23,52,26,31,43,29,27,35,41,50]

#if we order the data set by increasing value it could make it easier to search.
hops_ordered = [23,26,27,29,31,35,41,43,50,52]

search = int(input("what element value are you searching for? "))

#linear search on unordered list
for element in range(len(hops)):
    if hops[element] == search:
        print(f"value found at element {element + 1}. linear search (unordered)")
    elif element == len(hops):
        print("element value not found in data set")

#linear search in ordered list
for element in range(len(hops_ordered)):
    if hops_ordered[element] == search:
        print(f"value found at element {element + 1}. linear search (ordered)")
    elif element == len(hops_ordered):
        print("element value not found in data set")
    
#binary search
found = False
upper = len(hops_ordered)
lower = 0
while found == False:
    mid = (upper + lower)//2
    if search > hops_ordered[mid]:
        lower = mid + 1
    elif search < hops_ordered[mid]:
        upper = mid -1
    elif hops_ordered[mid] == search:
        print(f"element found at index {mid + 1}. binary search")
        found = True