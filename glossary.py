# Author: George Maysack-Schlueter
python_glossary = \
    {
        "list"            :
            "In Python, a list is a collection of ordered and mutable items "
            "enclosed in square brackets, capable of holding elements of "
            "various data types",
        "dictionary"      :
            "In Python, a dictionary is a built-in data structure that stores "
            "a collection of key-value pairs. It allows you to quickly access "
            "values using their associated keys. Dictionaries are enclosed in "
            "curly braces and each key is unique within the dictionary.",
        "for loop"        :
            "In Python, a for loop is a control structure used to iterate over "
            "a sequence (such as a list, tuple, or string) or other iterable "
            "objects. It allows you to execute a block of code repeatedly for "
            "each element in the sequence.",
        "conditional test":
            "In Python, a conditional test is a statement used to evaluate "
            "whether a certain condition is True or False. It's the foundation "
            "of making decisions in your code and controlling the flow of "
            "execution.",
        "function"        :
            "In Python, a function is a block of organized, reusable code that "
            "performs a specific task or set of tasks. It allows you to "
            "encapsulate logic and execute it by calling the function's name."
    }

for word in python_glossary:
    print(f"\nPython {word.title()} Definition:"
          f"\n{python_glossary[f'{word}']}")
