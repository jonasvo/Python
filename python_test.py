"""
Keywords:
with
try, except, finally
assert
immutable- variable cannot be changed
mutable- variable can be changed

//////////////////////////////////////////////////
decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify. Use with @decor (a function) above func()
Examples of other decorators:
@property- allows us to define a method but access it like an attribute
@classmethod- takes cls (class) as parameter instead of self
@staticmethod- behaves like plain functions, except for the fact that you can call them from an instance of the class.
Doesn't take either cls or self as parameter

//////////////////////////////////////////////////
Data Structures
Python supports the following data structures: lists, dictionaries, tuples, sets.
lists
Example:
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

Result:
>>>
Hello
world
!
>>>


dictionaries- only immutable objects can be used as keys to dictionaries
Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

Result:
>>>
24
42
>>>


tuples are very similar to lists, except that they are immutable. Also, they are created using parentheses, rather than square brackets.
Tuples can also be created without the parentheses, by just separating the values with commas.
Example:
words = ("spam", "eggs", "sausages",)
print(words[0])

Result:
>>>
spam
>>>


sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function.
They share some functionality with lists, such as the use of in to check whether they contain a particular item.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.

//////////////////////////////////////////////////
List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

Output:
>>>
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
>>>
[2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.
If a negative value is used for the step, the slice is done backwards.
Using [::-1] as a slice is a common and idiomatic way to reverse a list.

//////////////////////////////////////////////////
Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention,
and does not stop external code from accessing them.
_weakPrivMethod()

Strongly private methods and attributes have a double underscore at the beginning of their names.
This causes their names to be mangled, which means that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have
methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name.
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

"""
#////////////////////////////////////////////////////////////////////////////////////////////////////
"""
for i in range(5,-1, -1):
    print(i)

r = 0
while(r != 10):
    print(r)
    r += 1
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////
"""
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property #allows us to define a method but access it like an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ') #assign first with part before ' ' & last with last part after ' '
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def hoj(self):
        print("HELLO!")

    @hoj
    def my_hi(self):
        print("MyHi!")
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////
"""
emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
"""


class Person:
    def __init__(self, name = None, age = 0, sex = None):
        self.name = name
        self.age = age
        self.sex = sex
        self.id = 10

    def activity(self, action = "Sitting"):
        self.activity = action


class Student(Person):
    def __init__(self, id):
        self.id = id

    def subject(self, subject = None):
        self.subject = subject

katie = Person("Katie", 39, "F")

robert = Student(5)
robert.name = "Robert"
print robert.id


def decor1(func):
    def wrap1():
        print ("===")
        func()
        print ("===")
    return wrap1

def decor2(func):
    def wrap2():
        print ("ooo")
        func()
        print ("ooo")
    return wrap2


@decor1
@decor2
def printa():
    print ("Hello")

printa()
print decor1
