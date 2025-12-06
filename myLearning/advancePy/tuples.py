# Tuple: Ordered, immutable(not changable once defined), dupplicates allowed  --> ()

myTuple = ("Ramu", 23, True)
tup = ("ramu") 
# This is not a tuple now , python will consider this as a str value, for tup just add a comma after value if you have only one val tup = ("ramu", )

myTuple = (["Ramu", "2233", True])
print(myTuple, type(myTuple))

# indexing, slicing concept is same as list

my_tuple = ['a', 'p', 'p', 'l', 'e']
elm_count = my_tuple.count('p')
idx_val = my_tuple.index('a')

# Unpacking a tuple
data = "raj", "pooja", "kalaj"
name1, name2, name3 = data
print(name1, name2, name3)
print(type(data))

data2 = (0, 1, 2, 3, 4, 5)
num1, *num2, num3 = data2
print(num2)
print(num1, num2, num3)


"""
Tuples: test your comprehension:
- is it mutable or immutable?
- how to initialize a tuple?
- how to initialize a single-element tuple?
- how to convert list to tuple and vice versa?
- hot to get 1st element in tuple?
- how to unzip a tuple?
- how to count values in tuple?
- what does index() do?
"""

# data = input("Enter your data seperated by spaces ")
# print(data.split())

words =" ".join(list("spaces"))
print(words)