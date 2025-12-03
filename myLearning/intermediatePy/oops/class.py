"""
    class
    instance
    self(a naming standard for current object)
    instance attributes
    class attributes

    Use class attributes to define properties that should have the same value 
    for every class instance. Use instance attributes for properties that vary from one instance to another.

    Creating a new object from a class is called instantiating a class. 
    You can create a new object by typing the name of the class, followed by opening and closing parentheses:

    In this tutorial, you learned how to:

    Define a class, which is a sort of blueprint for an object
    Instantiate a class to create an object
    Use attributes and methods to define the properties and behaviors of an object
    Use inheritance to create child classes from a parent class
    Reference a method on a parent class using super()
    Check if an object inherits from another class using isinstance()

    Reference:
        https://realpython.com/python3-object-oriented-programming/
        https://realpython.com/python-class-constructor/
        https://realpython.com/python-classes/#special-methods-and-protocols
        https://realpython.com/python-double-underscore/

"""


class Employee:
    """
        Defined a simple class
        Having one class attribute and three instance attribute
        Also used 2 dunder methods (__init__ for assigning instance attribute value)
        __str__() for custom string represantation for the object
        attributes also known as properties
        methods also known as behaviour
    """
    company_name = "Mindfire Digital LLP"
    
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary


    def __str__(self):
        return f"{self.name} is working as {self.designation} with salary of {self.salary}"
    

# Class Instantiation
rajesh = Employee("Rajesh", "Sr. Software Engg", 100000)
beauty = Employee("Beauty", "Sr. Software Engg", 85000)
print(beauty)