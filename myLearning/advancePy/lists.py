# Lists: Ordered, mutable, duplicates allowed
data = ["rajehs", True, 500.25, 2000]

new_lst = list()

"""

len()
append()
extend()
pop()
remove()
insert()


"""


values = [1, 4, 5, 6, 3, 9, 2]
# Indexing (0 -based indexing)

# Positive Indexing
print(values[0]) #// 1
print(values[3]) #// 6

try:
    print(values[100])  #//  Throw IndexError because this index not exists in the above list
except IndexError:
    print("Index Error came")

# Negative Indexing
print(values[-1]) #// 2
print(values[-3]) #// 3

# Value membership check using in operator 
print(1 in values) #// True

# append method --> Used for appending a single elemnet at the end of the list
data.append("Begusarai")
print("After append", data)

# insert method --> used for add a single element at any index location in the list 
data.insert(1, "New data")
print("After insert", data)

# Add more than one elements at once in the list in the end of the list
data.extend(["A", "B", "C"])
print("After Extend", data)

