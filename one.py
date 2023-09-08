"""
starts with overview:
- basic building blocks of programming
- modules
- project: countdown app
- packages, PyPI and pip
- Project: automation with Python
- OOP - classes and objects
- Project - API request to GitLab

"""

#Strings & Numbers:
print(200, "is a great number")

print(20 * 24 * 60)


#String concatenation:
print(f"20 days are {20 * 24 * 60} minutes")


#Encapsulate Login in Functions:
"""
Allows us to not repeat logic, and encapsulate an action in one place
"""
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

"""
using return instead is also a possibility if we don't need to print a string
"""

days_to_units(35, "you are a *ick!")


#Scope:
"""
Discussion around global and local variables and in what data structures each are accessible.
"""


#Accepting User Input:
"""
gateways for users to access your codes actions
"""
your_name = input("What is your name? ")
print(your_name)


#Conditionals & If/Else (with comparison operators):
your_age = input("What is your age? (enter a number please) ")
arbitrary_old_age_no = 44

if int(your_age) > arbitrary_old_age_no:
    print("You're old! Bought a tombstone yet?")
else:
    print("You'll age like fine wine! Go enjoy life!")

"""
we could handle problems with invalid input in several ways. stripping out anything that isn't what we want? (regex).
Or we could use an .isdigit() builtin function and nesting the if/else written above inside the .isdigit function nested in a root if/else
"""


#Error Handling with Try/Except:
"""
You can next Try/Excepts within a function for example. The Try part will encapsulate the action you want to happen.
The Except part can be used to capture a system or logic response on the production of any one of Python's syntax, or runtime(exceptions).
"""


#While Loops:
"""
Use while loops to make a programme continue on until it reaches a predefined stop point.
"""


#Basic List Operations:
"""
- create a list: []
- use a specific element: name_of_list[element index int]
- add to end of list: name_of_list.append("element")
Used to store multiple items of data
"""


#Sets:
"""
Unlike lists, sets do NOT allow duplicate values
- set(name_of_set)
- add elements: name_of_set.add("name_of_element")
- remove elements: name_of_set.remove("name_of_element")
The .remove function works on BOTH sets and lists
"""


#Built-in Functions:
"""
Built-in functions within Python for each data type
These are easily searched for
"""


#Dictionary Data Type:
"""
Has key:value pairs
{"key": value, "key": value}
To get a value, we need to go via the key:
- 1) square brackets: name_of_dict["key_of_value_required"]
- 2) get() method: name_of_dict.get("key_of_value_required")

Summary of Python Data Types:
- Numeric: int, flt, complex
- String: str
- Sequence: list, tuple, range
- Binary: bytes, bytearray, memoryview
- Mapping: dict.
- Boolean: bool
- Sets: set, frozenset
- None: NoneType
"""


#Modules:
"""
Start off with Modules at 3:01:35
maybe do some code with it
"""

