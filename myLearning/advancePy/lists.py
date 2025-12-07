# Lists: Ordered, mutable, duplicates allowed  --> []
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

# Adding Element

# append method --> Used for appending a single elemnet at the end of the list
data.append("Begusarai")
print("After append", data)

# insert method --> used for add a single element at any index location in the list 
data.insert(1, "New data")
print("After insert", data)

# Add more than one elements at once in the list in the end of the list
data.extend(["A", "B", "C"])
print("After Extend", data)


# Removing element
# pop method --> Used to remove last element of a list and return back the same element
removed_element = data.pop()
print("removed_element", removed_element)


# pop method --> Used to remove a specific indexed value by index number 
del_elm_by_idx = data.pop(1)
print("del_elm_by_idx", del_elm_by_idx)

# remove method --> Used to remove element by actual value of element
rmv_elm = data.remove("A")
print(data)

# del keyword --> Used to delete a single (using idx) or many elements(using slicing) from any collections or whole collection

del data[0]
del data[1:3]

lst_data = ["2", "4"]
del lst_data

# clear method --> Using clear method we can just remove all the elements at once of a list
data.clear()
print(data)

# Manipulation methods

# sort mehtod --> Used for sorting 
values = [1, 4, 5, 6, 3, 9, 2]
values.sort()
print("sorted numbers",  values)

# sort method --> string values can be sorted by lexographical
words = ['grapes', 'banana', 'apple']
words.sort()
print("sorted words", words)

# reverse method --> Used for just reversing the order of elements
updated_data = [1, 'two', 3, 'sohan'] 
updated_data.reverse()
print("updated_reverse_data", updated_data)

# Note: sort() and reverse() method will apply in - place effect and will apply changes to the original list

# sorted method --> Used to sort a list elements and return a new list instead of changing original list
values = [1, 4, 5, 6, 3, 9, 2]
new_sorted_data = sorted(values)
print("new_sorted_data", new_sorted_data)


# reversed method --> Used to reverse the elements of a list and return those applied changes elements in a new list instaed of changing original list
updated_data = [1, 'two', 3, 'sohan'] 
new_reversed_data = list(reversed(updated_data))
print("new_reversed_data", new_reversed_data)

# You can create same element in a list as many times you want using a simple syntax
myList1 = [0] * 5
print(myList1)


myList2 = [101] * 5
print(myList2)


# We can concatenate 2 by using + operator
concatenated_list = myList1 + myList2
print("concatenated_list", concatenated_list)

# Slicing --> is a way to access sub part of list listVarName[start_idx: end_idx: step]
# default value of start_idx is 0 , end idx is len(listVarName) , default_step value is 1
# start_idx is inclusive and end_idx is exclusive
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Poistive Slicing (Left to Right)
print("Sub part of this list from idx 0 to 3 ", myList[0:4])
print("start value by default start at 0 and end to 5", myList[:4])
print("start value by from 1 and end to the default end", myList[1:])
print("start value by from default start and end to the default", myList[::2])

# Negative Slicing (Right to Left)
print("Sub part of this list from idx -1 to -5 ", myList[-1:-5])
print("start value by default start at 0 and end to 5", myList[-4:6:-1])
print("start value by from 1 and end to the default end", myList[-2:])
print("start value by from default start and end to the default", myList[::-2])

# using slicing just reverse all the elements
print("Reversed myList using slicing", myList[::-1])


lst_org = ["apple", "banana"]

lst_copy = lst_org 

lst_copy.append("mango")

print("List Copy", lst_copy)
print("List Org", lst_org)

# Note: Here (lst_copy = lst_org ) because of (= operateor ) assigmnet operator both lists refering same memory address in machine
# That means changing in one list will be affected another list too

# We can do actual copy in various ways mentioned below:
# copy method --> By using copy method we can create actual copy , now changing in copied list will not affect original list

lst_org = ["apple", "banana"]

lst_copy = lst_org.copy() # First way// shallow copy of the list
# lst_copy = list(lst_org) # Second  way
# lst_copy = lst_org[:] # Third way



lst_copy.append("mango")

print("1 List Copy", lst_copy)
print("1 List Org", lst_org)

# List Comprehension : Fast way to create a new list from existing list
# [expression for in loop]
myList = [1, 2, 3, 4, 5]
squares = [num * num for num in myList]
print("original list", myList)
print("squares", squares)


"""
Python lists, which are mutable ordered sequences of items, 
come with a variety of built-in methods for manipulation and interaction. 
Here are some of the most commonly used list methods: 

append(element): Adds a single element to the end of the list.

clear(): Removes all elements from the list, making it empty.

copy(): Returns a shallow copy of the list.

count(value): Returns the number of times a specified value appears in the list.

extend(iterable): Adds all elements from an iterable (like another list, tuple, or string) 
    to the end of the current list.

index(value, start, end): Returns the index of the first occurrence of a specified value 
    within the optional start and end indices. Raises a ValueError if the value is not found.

insert(index, element): Inserts an element at a specified index within the list.

pop(index): Removes and returns the element at the specified index. If no index is provided, 
    it removes and returns the last element.

remove(value): Removes the first occurrence of a specified value from the list. 
    Raises a ValueError if the value is not found.

reverse(): Reverses the order of the elements in the list in place.
sort(key=None, reverse=False): Sorts the elements of the list in place. 
    By default, it sorts in ascending order. 
You can customize the sorting with the key argument (for custom sorting logic) and reverse=True for descending order.
"""


