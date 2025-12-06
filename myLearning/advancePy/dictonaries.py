# Dictionary: Key-Value Pairs, Ordered, Mutable

student_info = {"name": "Rajesh", "age": 28}
# Adding new key value pair
student_info["test1_marks"] = 57
student_info["test2_marks"] = 87

student_info["email"] = "rjcse131998@gmail.com"

# If we will try to add another value for same key then for that key value will be overriden
student_info["email"] = "enggrajesh131998@gmail.com"

student_info["test3_marks"] = 97

# Deleting a key value from dict

# del keyword --> Here using del keyword removed a specific key value pair
del student_info["test1_marks"]
print(student_info)

# popitem method --> Using popitem method we can remove last key pair of the dict
last_key_val = student_info.popitem()
print("last_key_val", last_key_val)

# pop method --> Using pop method we can remove a specific key value pair
delete_name = student_info.pop('name')
print("delete_name", delete_name)
print(student_info)


# checking key inside a dict or not 
company_data = dict(name =  "Mindfire Digital LLP", revenue =  "1B", total_employee =  "500+")

# Using in operator
if "name" in company_data:
    print("Yes name key is there")

# using try-except 
try:
    print(company_data["last_revenue"])
except KeyError:
    print(f"KeyError: last_revenue key is not present in the comapny data dict")

# Loop through a dictionary

# By default looping over any dict will return key only
print("*" * 30)
for key in company_data:
    print(key)

# keys() method --> returns key only
print("*" * 30)
for key in company_data.keys():
    print(key)

# values() method --> returns value only
print("*" * 30)
for val in company_data.values():
    print(val)


# items() method --> returns key and value 
print("*" * 30)
for key, val in company_data.items():
    print(f"{key} ---> {val}")

# copy method
dict1 = {"name": "raj", "age": 23, "college": "bseb"}
cpy_dct = dict1
dict1["name"] = "pooja"
# Note : Here because of equal to assignment operator both variables 
# cpy_dct and dict1 will refer same memory address and due to this changes in one dict will be reflected in another too

# copy method --> Using copy method we can do actual copy
dict1 = {"name": "raj", "age": 23, "college": "bseb"}
cpy_dct = dict1.copy()
dict1["name"] = "pooja"

