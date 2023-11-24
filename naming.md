In Python, the naming conventions are influenced by the PEP 8 style guide. Here's a summary of when to use camelCase and snake_case:

snake_case:

Variables: For variable names, use lowercase words separated by underscores.

my_variable = 10

Function and Method Names: Function names and method names should also be in lowercase with underscores separating words.

def my_function():
    pass

Module Names and File Names: It's recommended to use all lowercase names, and underscores can be used to improve readability.

my_module.py

Non-public Attributes/Methods: For internal use (private members) use a single leading underscore.

def _private_method():
    pass

CamelCase:

Class Names: Use CapWords (another term for CamelCase) convention. First letter of each word is capitalized, and there are no underscores between words.

class MyClass:
    pass

Exceptions: By convention, exceptions should also follow the CamelCase naming.

class MyError(Exception):
    pass

Remember:

Constants should be in uppercase with underscores separating words.

MAX_SIZE = 100

Avoid using single-character variable names like l, O, or I since they can be confused with numbers.

In practice, the convention you choose largely depends on the context. When writing Python code, it's always a good idea to follow PEP 8 to make your code more readable and maintainable by others in the Python community. However, if you're interacting with libraries or systems that use a different naming convention (like a JavaScript framework), you might need to adjust your naming strategy to match that ecosystem.