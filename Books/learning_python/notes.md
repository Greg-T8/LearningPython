# Notes from "Learning Python" by Mark Lutz

<img src='images/20250409025850.png' width='250'/>

<details>
<summary>Book Resources</summary>

- [Book Code](https://learning-python.com/LP6E-code)
- [Python Documentation](https://docs.python.org/3/)

</details>

<!-- omit in toc -->
## Contents
- [Part II. Objects and Operations](#part-ii-objects-and-operations)
  - [4. Introducing Python Objects](#4-introducing-python-objects)
    - [Strings](#strings)
      - [Sequence Operations](#sequence-operations)
      - [Immutability](#immutability)
      - [Type-Specific Methods](#type-specific-methods)
      - [Getting Help](#getting-help)
      - [Other Ways to Code Strings](#other-ways-to-code-strings)
      - [Unicode Strings](#unicode-strings)
    - [Lists](#lists)
      - [Sequence Operations](#sequence-operations-1)
      - [Type-Specific Operations](#type-specific-operations)
      - [Bounds Checking](#bounds-checking)
      - [Nesting](#nesting)
      - [Comprehensions](#comprehensions)
    - [Dictionaries](#dictionaries)
      - [Mapping Operations](#mapping-operations)
      - [Nesting Revisited](#nesting-revisited)
      - [Missing Keys: `if` Tests](#missing-keys-if-tests)
      - [Item Iteration: `for` Loops](#item-iteration-for-loops)
    - [Tuples](#tuples)
      - [Why Tuples?](#why-tuples)
    - [Files](#files)
      - [Unicode and Byte Files](#unicode-and-byte-files)
    - [Other Object Types](#other-object-types)
      - [Sets](#sets)
      - [Booleans and None](#booleans-and-none)
      - [Types](#types)
      - [Type Hinting](#type-hinting)
  - [5. Numbers and Expressions](#5-numbers-and-expressions)
    - [Numeric Object Basics](#numeric-object-basics)
      - [Numeric Literals](#numeric-literals)
      - [Built-in Numeric Tools](#built-in-numeric-tools)
    - [Python Expression Operators](#python-expression-operators)
      - [Mixed Types Are Converted Up](#mixed-types-are-converted-up)
      - [Preview: Operator Overloading and Polymorphism](#preview-operator-overloading-and-polymorphism)
    - [Numbers in Action](#numbers-in-action)
      - [Variables and Basic Expressions](#variables-and-basic-expressions)
      - [Numeric Display Formats](#numeric-display-formats)
      - [Comparison Operators](#comparison-operators)
      - [Division Operators](#division-operators)
      - [Integer Precision](#integer-precision)
      - [Complex Numbers](#complex-numbers)
      - [Hex, Octal, and Binary](#hex-octal-and-binary)
      - [Bitwise Operators](#bitwise-operators)
      - [Underscore Separators in Numbers](#underscore-separators-in-numbers)
      - [Other Built-In Numeric Tools](#other-built-in-numeric-tools)
    - [Other Numeric Objects](#other-numeric-objects)


## Part II. Objects and Operations

### 4. Introducing Python Objects

**The Python Conceptual Hierarchy**:  
1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

**Python's Core Object Types**:  

| Object type            | Example literals/creation                                         |
| ---------------------- | ----------------------------------------------------------------- |
| Numbers                | `1234`, `3.1415`, `0b111`, `1_234`, `3+4j`, `Decimal`, `Fraction` |
| Strings                | `'code'`, `"app's"`, `b'a\x01c'`, `'h\u00c4ck'`, `'Häck🐍'`        |
| Lists                  | `[1, [2, 'three'], 4.5]`, `list(range(10))`                       |
| Dictionaries           | `{'job': 'dev', 'years': 40}`, `dict(hours=10)`                   |
| Tuples                 | `(1, 'app', 4, 'U')`, `tuple('hack')`, `namedtuple`               |
| Files                  | `open('docs.txt')`, `open(r'C:\data.bin', 'wb')`                  |
| Sets                   | `set('abc')`, `{'a', 'b', 'c'}`                                   |
| Other core objects     | `Booleans`, `types`, `None`                                       |
| Program-unit objects   | `Functions`, `modules`, `classes`                                 |
| Implementation objects | `Compiled code`, `stack tracebacks`                               |

#### Strings

##### Sequence Operations

Python allows referencing index positions in strings using square brackets `[]`:  
```python
>>> S = 'Code'
>>> len(S)
4
>>> S[0]
'C'
>>> S[1]
'o'
>>> 
```
You can also index backwards using negative numbers:
```python
>>> S[-1]
'e'
>>> S[-2]
'd'
```
More formally, a negative index is added to the length of the string to yield a positive offset:
```python
>>> S[-1]
'e'
>>> S[len(S)-1]
'e'
Slicing allows you to extract a section, providing everything from the start index up to but not including the end index:
```python
>>> S
'Code'
>>> S[1:3]        # Slicing from index 1 to 2 (3 is excluded)
'od'
```
- The left bound defaults to 0 and the right bound defaults to the length of the sequence being sliced:
```python
>>> S
'Code'
>>> S[1:]          # Slicing from index 1 to the end of the string
'ode'
>>> S[0:3]         # Slicing from index 0 to 2 (3 is excluded)
'Cod'
>>> S[:3]          # Slicing from index 0 to 2 (3 is excluded)
'Cod'
>>> S[:-1]         # Slicing from index 0 to -1 (last character excluded)
'Cod'
>>> S[:]           # Slicing from index 0 to the end of the string
'Code'
```
Strings also support concatenation and repetition: 
```python
>>> S
'Code'
>>> S + 'xyz'        # S remains unchanged
'Codexyz'
>>> S
'Code'
>>> S * 8
'CodeCodeCodeCodeCodeCodeCodeCode'
```

##### Immutability

Strings are immutable, meaning they cannot be changed in place: 
```python
>>> S
'Code'
>>> S[0] = 'z'
Traceback (most recent call last):
  File "<python-input-34>", line 1, in <module>
    S[0] = 'z'
    ~^^^
TypeError: 'str' object does not support item assignment
```
You can, however, run expressions to make new objects:
```python
>>> S = 'Z' + S[1:]
>>> S
'Zode'
```
The following core object types are immutable:  
- Strings
- Numbers
- Tuples

You can change text-based data in place if you use a mutable object type, such as a list.
```python
>>> S = 'Python'
>>> L = list(S)
>>> L
['P', 'y', 't', 'h', 'o', 'n']
>>> L[0] = 'C'
>>> ''.join(L)
'Cython'
```
The following example shows you can use a `bytearray`  to support in-place changes: 
```python
>>> B = bytearray(b'app')
>>> B.extend(b'lication')
>>> B
bytearray(b'application')
>>> B.decode()
'application'
```
> A `bytearray` is a mutable sequence of bytes--essentially, it's like a list of bytes that you can modify.

##### Type-Specific Methods

The `find()` and `replace()` methods are used to search and replace substrings in strings: 
```py
>>> S = 'Code'
>>> S.find('od')
1
>>> S
'Code'
>>> S.replace('od', 'abl')
'Cable'
>>> S
'Code'
```
Note the original string remains unchanged. 

Other methods:
```py
>>> line = 'aaa,bbb,cccc,dd'
>>> line.split(',')                   # Splits the string on a delimiter into a list of substrings
['aaa', 'bbb', 'cccc', 'dd']

>>> S = 'code'
>>> S.upper()                         # Upper- and lowercase conversions
'CODE'

>>> S.isalpha()                       # Content tests: isalpha, isdigit, etc.
True

>>> line = 'aaa,bbb,cccc,dd\n'
>>> line.rstrip()                     # Remove whitespace from the right side of the string
'aaa,bbb,cccc,dd'

>>> line = 'aaa,bbb,cccc,dd\n'
>>> line.rstrip().split(',')          # Combining two operations, left to right
['aaa', 'bbb', 'cccc', 'dd']
```

Three formatting operations are available: 
```py
>>> 'Using %s version %s.%s' % (tool, major, minor + 9)       # Format expression, known as the old-style string formatting
'Using Python version 3.12'

>>> 'Using {} version {}.{}'.format(tool, major, minor + 9)   # Format method, newer
'Using Python version 3.12'

>>> f'Using {tool} version {major}.{minor + 9}'               # f-string, the newest
'Using Python version 3.12'
```
All three methods resolve substitution values and build new strings when they are run.

Each form is rich with features and matter most when generating readable output and numeric reports:

```py
>>> '%.2f | %+05d' % (3.14159, -62)                   # Digits, signs, padding
'3.14 | -0062'

>>> '{1:,.2f} | {0}'.format('sapp'[1:], 29699.256)    # Commas, decimal digits
'29,699.26 | app'

>>> f'{296999.256:,.2f} | {'sapp'[1:]}'               # Ditto, with nested quotes
'296,999.26 | app'
```

##### Getting Help

Use the built-in `dir()` function to list the attributes of an object: 
```py
>>> S = 'Code'
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
Names without the underscores are all the callable methods on string objects. Names with the double underscores are used for operator overloading in classes.

Example showing how concatenation ultimately works by calling the `__add__` method: 
```py
>>> S + 'head!'
'Codehead!'

>>> S .__add__('head!')
'Codehead!'
```

The `dir()` function simply lists names. Use the `help()` function to get more information about a specific method: 
```py
>>> help(S.replace)
Help on built-in function replace:

replace(old, new, /, count=-1) method of builtins.str instance
    Return a copy with all occurrences of substring old replaced by new.

      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are
    replaced.
```

##### Other Ways to Code Strings

```py
>>> S = 'A\nB\tC'   # Escapes: newline and tab
>>> len(S)          # Each stands for one character
5

>>> S = 'A\0B\0C'   # \0 is a binary zero byte, does not terminate the string
>>> len(S)          # Length remains 5, despite the nulls
5

>>> S
'A\x00B\x00C'       # Nonprintables are displayed as \xNN hex escapes
```

Python supports multiline strings using triple quotes: 
```py
>>> msg = """
... aaaaaaaaaaaa
... bbb'''bbb""bb
... ccccccccc
... """

>>> msg
'\naaaaaaaaaaaa\nbbb\'\'\'bbb""bb\nccccccccc\n'
```

Python also supports raw strings, which do not interpret backslashes as escape characters.
```py
>>> msg = r'C:\Users\you\code'
>>> msg
'C:\\Users\\you\\code'
```

##### Unicode Strings

```py
>>> 'hÄck'      # Normal strings are Unicode text
'hÄck'
>>> b'a\x01c'   # Bytes are binary data, not Unicode text
b'a\x01c'
``` 
Python's byte strings are sequences of 8-bit *bytes* that print with ASCII characters when possible. Python's text strings are sequences of *Unicode code points*, which do not map to single bytes store in memory or encoded in files.

```py
>>> 'Code'                        # Characters may be any size in memory
'Code'
>>> 'Code'.encode('utf-8')        # Encoded to 4 bytes in UTF-8 in files
b'Code'
>>> 'Code'.encode('utf-16')       # Encoded to 10 bytes in UTF-16 in files
b'\xff\xfeC\x00o\x00d\x00e\x00' 
```

To code non-ASCII characters, use `\x` hexadecimal escapes; short `\u` or long `\U` Unicode escapes:
```py
>>> 'h\xc4\u00c4\U000000c4Äck'
'hÄÄÄÄck'
```
In text strings, each of these forms specify Unicode code points. By contrast, byte strings use only `\x` hexadecimal escapes to embed the values of *raw* bytes.

```py
>>> '\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1')
('£', b'\xa3', '£')
```

#### Lists

##### Sequence Operations

```py
>>> L = [123, 'text', 1.23]   # A list of different-type objects
>>> len(L)
3
```

You can index and slice lists in the same way as strings: 
```py
>>> L[0]                                    # Indexing by position (offset)
123

>>> L[:-1]                                  # Slicing from index 0 to -1 (last item excluded)
[123, 'text']

>>> L + [4, 5, 6]                           # Concatenation of two lists
[123, 'text', 1.23, 4, 5, 6]

>>> L * 2                                   # Repetition of a list
[123, 'text', 1.23, 123, 'text', 1.23]

>>> L 
[123, 'text', 1.23]                         # Original list remains unchanged
```

##### Type-Specific Operations

Unlike arrays in other languages, lists have no fixed size or type and are mutable:
```py
>>> L.append('Py')          # Growing: add to the end of the list
>>> L
[123, 'text', 1.23, 'Py']

>>> L.pop(2)                # Shrinking: remove and return the item at index 2
1.23

>>> L                       # Original list is changed in place
[123, 'text', 'Py']

>>> del L[2]                # Shrinking: remove the item at index 2
>>> L
[123, 'text']
```

Other list methods:
```py
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']

>>> M.reverse()
>>> M
['cc', 'bb', 'aa']
```

##### Bounds Checking

Python does not allow you to index or assign to a list outside its bounds:
```py
>>> L
[123, 'text', 'Py']

>>> L[99]
Traceback (most recent call last):
  File "<python-input-49>", line 1, in <module>
    L[99]
    ~^^^^
IndexError: list index out of range

>>> L[99] = 1
Traceback (most recent call last):
  File "<python-input-51>", line 1, in <module>
    L[99] = 1
    ~^^^^
IndexError: list assignment index out of range
```
To grow a list, use the `append()` method or make a new list.

##### Nesting

```py
>>> M = [[1, 2, 3],                 # Create a 3 x 3 matrix as a nexted list
... [4, 5, 6],
... [7, 8, 9]]

>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> M[1]                            # Get row 2
[4, 5, 6]

>>> M[1][2]                         # Get row 2, then get item 3 within that row
6 
```

##### Comprehensions

A *list comprehension expression* enable you to build a new list by running an expression on each item in a sequence:
```py
>>> col2 = [row[1] for row in M]      # Collect the items in column 2

>>> col2
[2, 5, 8]

>>> M                                 # Original list remains unchanged
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
List comprehensions are composed of an expression and a looping construct:

```py
>>> [row[1] + 1 for row in M]
[3, 6, 9]

>>> [row[1] for row in M if row[1] % 2 == 0]
[2, 8]
```
Using a list comprehension to step over a hardcoded list of coordinates and a string:
```py
>>> diag = [M[i][i] for i in [0, 1, 2]]   # Collect a diagnonal from matrix
>>> diag
[1, 5, 9]

>>> doubles = [c * 2 for c in 'hack']     # Repeat characters in a string
>>> doubles
['hh', 'aa', 'cc', 'kk']
```

Using a `range`:
```py
>>> list(range(4))                                            # Integers 0..(N-1)
[0, 1, 2, 3]

>>> list(range(-6, 7, 2))                                     # -6 to +6, by 2
[-6, -4, -2, 0, 2, 4, 6]


>>> [[x ** 2, x ** 3] for x in range(4)]                      # Multiple values, "if" filters
[[0, 0], [1, 1], [4, 8], [9, 27]]

>>> [[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]    # // means integer division
[[2, 1, 4], [4, 2, 8], [6, 3, 12]]
```

Enclosing list comprehensions in parentheses creates a generator expression, which is an iterator that generates items on demand:
```py
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

>>> G = (sum(row) for row in M)   # Make a generator of row sums

>>> next(G)
6
>>> next(G)
15
>>> next(G)
24
```
Comprehension syntax can be used to create *sets* and *dictionaries* as well:
```py
>>> {sum(row) for row in M}           # Makes an unordered set of row sums
{24, 6, 15}

>>> {i: sum(M[i]) for i in range(3)}  # Makes a dictionary of row sums
{0: 6, 1: 15, 2: 24}
```

#### Dictionaries

Python dictionaries are the only core member of a category known as *mappings*. Mappings store objects by key instead of by relative position.

Dictionaries are mutable: they may be changed in place and grow and shrink as needed.

##### Mapping Operations

```py
>>> D = {'name': 'Pat', 'job': 'dev', 'age': 40}

>>> D['name']
'Pat'

>>> D['job'] = 'mgr'
>>> D
{'name': 'Pat', 'job': 'mgr', 'age': 40}
```

It's more common to see dictionaries built up in different ways:

```py
>>> D = {}
>>> D['name'] = 'Pat'
>>> D['job'] = 'dev'
>>> D['age'] = 40
>>> D
{'name': 'Pat', 'job': 'dev', 'age': 40}
```

There are also methods for passing to the `dict` type naem either *keyword arguments* or the result of *zipping* together sequences of keys and values:

```py
>>> pat1 = dict(name='Pat', job='dev', age=40)                          # keywords
>>> pat1
{'name': 'Pat', 'job': 'dev', 'age': 40}

>>> pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))        # Zipping
>>> pat2
{'name': 'Pat', 'job': 'dev', 'age': 40}
```
**Note:** Starting with Python 3.7, dictionary keys retain their *insertion order*: the order of keys  is the order in which keys were added.

##### Nesting Revisited


```py
>>> rec = {'name': {'first': 'Pat', 'last': 'Smith'},   # 'name' is a nested dictionary
...        'jobs': ['dev', 'mgr'],
...        'age': 40.5}

>>> rec['name']                                         # Index the nested dictionary
{'first': 'Pat', 'last': 'Smith'}

>>> rec['name']['last']
'Smith'

>>> rec['jobs']                                         # 'jobs' is a nested list
['dev', 'mgr']

>>> rec['jobs'][-1]                                     # Index the nested list
'mgr'

>>> rec['jobs'].append('janitor')                       # Expand Pat's job description in place
>>> rec
{'name': {'first': 'Pat', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}
```

Nesting in Python provides flexibility over C. Building a similar structure in C would require much more code: you would have to lay out and declare structures and arrays, fill out values, link everything together, and so on.

In lower-level languages, you would have to allocate *memory* space for objects ahead of time and be careful to release it when you are done. In Python, object memory allotted as needed and freed when we lose the last reference to it&mdash;by assigning its variable to something else:

```py
>>> rec = 0     # Now the prior object's space is reclaimed
```

##### Missing Keys: `if` Tests

Dictionaries also support type-specific operations with *methods*:

```py
>>> D = {'a': 1, 'b': 2, 'c': 3}        # Assigning new keys grows dictionaries
>>> D['d'] = 4
>>> D
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

>>> D['e']                              # Referencing a missing key raises an error
Traceback (most recent call last):
  File "<python-input-57>", line 1, in <module>
    D['e']
    ~^^^^^
KeyError: 'e'
```
How do you handle such errors? 

```py
>>> 'e' in D
False

>>> if not 'e' in D:
...    print('missing key!')
... 
missing key!
```

You can also use the `get()` method to return a default value if the key is missing:
```py
>>> D.get('a', 'missing')           # Like D['a'] but with a default value
1
>>> D.get('e', 'missing')           # Default returned if absent
'missing'
>>> 
>>> D['e'] if 'e' in D else 0       # if/else ternary expression form
0
```

##### Item Iteration: `for` Loops

Use the `keys`, `values`, or `items` methods to get the keys, values, or key-value pairs:

```py
>>> D = dict(a=1, b=2, c=3)
>>> D
{'a': 1, 'b': 2, 'c': 3}

>>> list(D.keys())
['a', 'b', 'c']

>>> list(D.values())
[1, 2, 3]

>>> list(D.items())
[('a', 1), ('b', 2), ('c', 3)]
```

You dcan use an iterator to step through the keys, values, or items:
```py
>>> D.keys()                    # Get an iterable object
dict_keys(['a', 'b', 'c'])

>>> I = iter(D.keys())          # Get an iterator from an iterable

>>> next(I)                     # Get one result at a time from iterator
'a'
>>> next(I)                     
'b'
```
Iterators are useful because they can save memory by not producing all their results at once.

You can usually forget the iterator details by using a `for` loop:
```py
>>> for key in D.keys():                # Auto run the iteration protocol
...        print(key, '=>', D[key])     # Display multiple items, space between
... 
a => 1
b => 2
c => 3
```

The `for` loop can help you step through keys implicitly as well as key/value pairs:

```py
>>> for key in D:                       # Implicit keys() iteration
...        print(key, '=>', D[key])
... 
a => 1
b => 2
c => 3

>>> for (key, value) in D.items():      # Key/value-pair tuples iteration
...        print(key, '=>', value)
... 
a => 1
b => 2
c => 3
```

#### Tuples

Functionally, tuples are used to represent fixed collections of items: the components of a specific calendar date, the coordinates of a point in space, or the fields of a database record.

Syntactically, tuples are coded using parentheses `()` instead of square brackets `[]`, which makes them easy to distinguish from lists. Tuples support arbitrary nesting, and the usual sequence operations, such as indexing, slicing, and concatenation.

```py
>>> T = (1, 2, 3, 4)        # A 4-item tuple
>>> len(T)
4

>>> T + (5, 6)              # Concatenation: a new tuple
(1, 2, 3, 4, 5, 6)

>>> T[0], T[1:]             # Indexing, slicing, and more
(1, (2, 3, 4))
```

Tuples have type-specific callable methods, but not nearly as many as lists:

```py
>>> T.index(4)      # Tuple methods: 4 appears at offset 3
3

>>> T.count(4)      # 4 appears once
1
```

Tuples cannot be changed once created. One-item tuples require a trailing comma:

```py
>>> T[0] = 2                    # Tuples are immutable
Traceback (most recent call last):
  File "<python-input-109>", line 1, in <module>
    T[0] = 2
    ~^^^
TypeError: 'tuple' object does not support item assignment

>>> T = (2,) + T[1:]            # One-item tuples require a trailing comma
>>> T
(2, 2, 3, 4)
```

Like lists and dictionaries, tuples suport mixed types and nesting, but they don't grow and shrink like lists nad dictionaries because they are immutable:

```py
>>> T = 'hack', 3.0, [11, 22, 33]
>>> T
('hack', 3.0, [11, 22, 33])

>>> T[1]
3.0
>>> T[2][1]
22

>>> T.append(4)
Traceback (most recent call last):
  File "<python-input-120>", line 1, in <module>
    T.append(4)
    ^^^^^^^^
```

##### Why Tuples?

Tuples are not used as often as lists, but their immutablility is the whole point. 

Tuples provide an integrity constraint that is convenient in larger programs: if you pass a collection of objects around as a list, it can be changed anywhere; if you use a tuple, it can't be changed.

#### Files

To create a file object, use the built-in `open()` function, which returns a file object that can be used to read or write data:

```py
>>> f = open('data.txt', 'w')   # Open a new file in text-output mode; create if it doesn't exist
>>> f.write('Hello\n')          # Write strings of characters to it
6
>>> f.write('world!\n')         # Return number of items written
7
>>> f.close()                   # Close to flush output buffers to disk
```

You can use the `r` mode to read from a file, which is also the default if you omit the mode in the call. A file's content is always a string, regardless of the type of data it contains:

```py
>>> f = open('data.txt')        # Open an existing file in text-input mode
>>> text = f.read()             # Read entire file into a string
>>> text
'Hello\nWorld!\n'

>>> print(text)                 # print interprets control characters
Hello
World!

>>> text.split()                # File content is always a string
['Hello', 'World!']
```

Though, the best way to read a text file is usually not to read it all&mdash;files support the *iteration protocol* with an iterator that automatically reads line by line in `for` loops:

```py
>>> for line in open('data.txt'):       # Display lines in a file
...     print(line.rstrip())            # Single spaced (sans \n)
...
Hello
World!
```

##### Unicode and Byte Files

Python text files always use Unicode encoding to encode strings on writes and decode strings on reads. However, binary files, which are useful for processing non-text data, e.g. media, data created by C programs, and so on, are also supported.

```py
>>> bf = open('data.bin', 'wb')         # Open a new file in binary-output mode
>>> bf.write(b'h\xFFa\xEEc\xDDk\n')     # Write binary data to it
8

>>> bf.close()                          
>>> open('data.bin', 'rb').read()       # Read the file in binary-input mode
b'h\xffa\xeec\xddk\n'
```

When it comes to text files, if you want your code to work across platforms, you should generally make encodings explicit to avoid surprises:

```py
>>> tf = open('unidata.txt', 'w', encoding='utf-8')
>>> tf.write('\U0001f40d\u0068\u00c4\u0063\u006b\U0001f44f')    # Encodes to UTF-8
6
>>> tf.close()

>>> open('unidata.txt', 'r', encoding='utf-8').read()           # Decodes from UTF-8
'🐍hÄck👏'
>>> open('unidata.txt', 'rb').read()                            # Raw encoded text
b'\xf0\x9f\x90\x8dh\xc3\x84ck\xf0\x9f\x91\x8f'
```

While files automate most encodings, you can also encode and decode manually if your program gets Unicode data from another source&mdash;parsed from an email message or fetched over a network connection, for example:

```py
>>> 'hÄck'.encode('utf-8')
b'h\xc3\x84ck'

>>> b'h\xc3\x84ck'.decode('utf-8')
'hÄck'
```

#### Other Object Types

##### Sets

Python sets are unordered collections of immutable (technically "hashable") objects, which store each object just once. You create sets by using the built-in `set` function:

```py
>>> X = set('hack')                     # Sequence => set
>>> Y = {'a', 'p', 'p'}                 # Set literal
>>> X, Y
({'c', 'k', 'a', 'h'}, {'p', 'a'})

>>> X & Y, X | Y                        # Intersection, union
({'a'}, {'c', 'a', 'h', 'k', 'p'})

>>> X - Y, X > Y                        # Difference, superset
({'c', 'k', 'h'}, False)
```

Sets are useful for filtering out duplicates, isolating differences, and performing order-neutral equality tests without sorting:

```py
>>> list(set([3, 1, 2, 1, 3, 1]))       # Remove duplicates
[1, 2, 3]

>>> set('code') - set('hack')           # Collection difference
{'e', 'd', 'o'}

>>> set('code') == set('deoc')          # Order-neutral equality
True
```

##### Booleans and None

Python Booleans are predefined `True` and `False` objects that are essentially integers 1 and 0, respectively with custom display logic. There is also a special placeholder object called `None`, which is used to initialize names and objects and designate an absence of a result in functions:

```py
>>> 1 > 2, 1 < 2            # Booleans
(False, True)

>>> bool('hack')            # All objects have a Boolean value
True                        # Nonempty means True

>>> X = None                # None placeholder
>>> print(X)                # But None is a thing
None

>>> L = [None] * 100        # Initialize a list with 100 None objects
>>> L
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

```

##### Types

The `type` object, returned by the built-in `type()` function, is an object that gives the type of another object.

```py
>>> L = [1, 2, 3]

>>> type(L)         # Tye type of a list object
<class 'list'>

>>> type(type(L))   # Even types are objects
<class 'type'>
```

The `type` object allows you to check the types of the objects it processes:

```py
>>> type(L) == type([])     # Type testing using a real object
True

>>> type(L) == list         # Type testing using a type name
True

>>> isinstance(L, list)     # The object-oriented way to test types
True
```

The author notes that type checking is not the "Pythonic" way to write code. Reason being is that type checking leads to code that is less flexible and more brittle, as it relies on specific types rather than the behavior of objects. Rather than checking types, Python encourages you to code to object interfaces, not to types. This means you should focus on what an object *does*, not what it *is*.

##### Type Hinting

Python has slowly accumulated a type-declaration facility known as *type hinting*, based on earlier function annotations and insipired by TypeScript.

With these syntax and module extensions, it is possible to name expected object types of function arguments and results, attributes in class-based objects, and even simple variables.

```py
>>> x: int = 1          # Optional hint: x might be an integer
>>> x = 'anything'      # But it doesn't have to be!
```

Type hinting is only meant for documentation and use by third-party tools, such as type checkers and IDEs. The Python language does not itself mandate or use type declarations.

### 5. Numbers and Expressions

This chapter begins the in-depth coverage of the Python language.

#### Numeric Object Basics

Python's numeric toolbox includes:
- Integer and floating-point numbers
- Complex number objects
- Decimal and fixed-precision objects
- Fraction rational number objects
- Set objects and operations
- Boolean and bitwise operations
- Built-in modules, such as `math`, `cmath`, `random`, and `statistics`
- Third-party add-ons, including vectors, visualization, plotting, and extended precision

##### Numeric Literals

| Literal                             | Interpretation                       |
| ----------------------------------- | ------------------------------------ |
| 1234, -24, 0, 9_999_999_999_999     | Integers (unlimited size)            |
| 1.23, 1., 3.14e-10, 4E210, 4.0e+210 | Floating-point numbers               |
| 0o177, 0x9ff, 0b101010              | Octal, hex, and binary literals      |
| 3+4j, 3.0+4.0j, 3J                  | Complex number literals              |
| set('hack'), {1, 2, 3, 4}           | Sets: constructors and literals      |
| Decimal('1.0'), Fraction(1, 3)      | Decimal and fraction extension types |
| bool(X), True, False                | Boolean type and constants           |

##### Built-in Numeric Tools

- Expression Operators: `+`, `-`, `*`, `/`, `>>`, `**`, `&`, `%`, etc.
- Built-in mathematical functions: `pow`, `abs`, `round`, `int`, `hex`, `bin`, etc.
- Utility modules: `random`, `math`, `statistics`, etc.

#### Python Expression Operators

The following list of operators is ordered by precedence. Operators lower in the table have higher precedence.

| Operators                            | Description                                                       |
| ------------------------------------ | ----------------------------------------------------------------- |
| `yield x`, `yield from x`            | Generator function `send` protocol                                |
| `x := y`                             | Assignment expression                                             |
| `lambda args: expression`            | Anonymous function generation                                     |
| `x if y else z`                      | Ternary selection (`x` is evaluated only if `y` is true)          |
| `x or y`                             | Logical OR (`y` is evaluated only if `x` is false)                |
| `x and y`                            | Logical AND (`y` is evaluated only if `x` is true)                |
| `not x`                              | Logical negation                                                  |
| `x in y`, `x not in y`               | Membership (iterables)                                            |
| `x is y`, `x is not y`               | Object identity tests                                             |
| `x < y`, `x <= y`, `x > y`, `x >= y` | Magnitude comparison, set subset and superset                     |
| `x == y`, `x != y`                   | Value equality operators                                          |
| `x \| y`                             | Bitwise OR, set union, dictionary merge                           |
| `x ^ y`                              | Bitwise XOR, set symmetric difference                             |
| `x & y`                              | Bitwise AND, set intersection                                     |
| `x << y`, `x >> y`                   | Shift `x` left or right by `y` bits                               |
| `x + y`                              | Addition, concatenation                                           |
| `x - y`                              | Subtraction, set difference                                       |
| `x * y`                              | Multiplication, repetition                                        |
| `x % y`                              | Remainder, format                                                 |
| `x / y`, `x // y`                    | Division: true and floor                                          |
| `x @ y`                              | Matrix multiplication (unused by Python, i.e. you must implement) |
| `-x`, `+x`, `~x`                     | Negation, identity, bitwise NOT (inversion)                       |
| `x ** y`                             | Power (exponentiation)                                            |
| `await x`                            | Await expression (async functions)                                |
| `x[i]`                               | Indexing (sequence, mapping, others)                              |
| `x[i:j:k]`                           | Slicing                                                           |
| `x(...)`                             | Call (function, method, class, other callable)                    |
| `x.attr`                             | Attribute reference                                               |
| `(...)`                              | Tuple, expression, generator expression                           |
| `[...]`                              | List, list comprehension                                          |
| `{...}`                              | Dictionary, set, dictionary and set comprehensions                |

**Note:** the Python no-ops character, `@`, is used to introduce function decorators, but not as an expression operator.

##### Mixed Types Are Converted Up

Operands in expresssions are converted up to the most complicated operand, and then math is performed on the operands.

```py
>>> 40 + 3.14       # Integer to float, float math/result
43.14
```

You can call built-in functions to convert types manually:

```py
>>> int(3.1415)
3
>>> float(3)
3.0
```

However, you usually don't need to do this because Python automatically converts up to the more complex type within an expression.

Keep in mind that Python only does this for numeric objects in an expression. In general, Python does not convert across any other type boundaries automatically.

##### Preview: Operator Overloading and Polymorphism

All Python operators may be overloaded by Python classes and C extension types to work on objects you create. For example, objects coded with classes may be added or concatenated with `x + y` expressions, indexed with `x[i]`, and so on.

#### Numbers in Action

##### Variables and Basic Expressions

```py
>>> a = 3
>>> b = 4

>>> a + 1, a - 1            # Addition, subtraction
(4, 2)

>>> b * 3, b / 2            # Multiplication, division
(12, 2.0)

>>> a % 2, b ** 2           # Remainder, exponentiation
(1, 16)

>>> 4 + 4.0, 2.0 ** b       # Mixed types: int to float, float math
(8.0, 16.0)
```

**Note:** Lines with two expressions return a tuple of results.

Demonstrating operator grouping and precedence:

```py
>>> b / 2 + a       # Same as ((4 / 2) + 3)
5.0

>>> b / (2 + a)     # Same as (4 / (2 + 3))
0.8
```

Python performs *true* division, which always retains fractional remainders and gives a floating-point result. You can force a fractional result by coding `2.0` instead of `2` or you can use floor division, `//`, which discards the decimal digits in the result, returning truncated floating-point for floats:

```py
>>> a, b                
(3, 4)

>>> b // 2 + a          # Floor division: integer
5
>>> b // (2 + a)        # Truncates fraction (for positives)
0

>>> b // 2.0 + a        # Auto-conversions: returns truncated floating-points
5.0
>>> b // (2.0 + a)
0.0
```

##### Numeric Display Formats

The results of some expressions may look odd:

```py
>>> 1.1 + 2.2
3.3000000000000003          # What's up with the 3 at the end?

>>> print(1.1 + 2.2)
3.3000000000000003
```

Reason has to do with limitations in floating-point representation and its inability to represent some values in a limited number of bits.

You can force the issue with string formatting:

```py
>>> num = 1.1 + 2.2
>>> num
3.3000000000000003

>>> '%e' % num                  # String-formatting expression
'3.300000e+00'

>>> '%.1f' % num                # Alternative floating-point format
'3.3'

>>> f'{num:e}', f'{num:.1f}'    # F-string formatting
('3.300000e+00', '3.3')
```

**Note:** The default output format of interactive echoes and `print` correspond to the built-in `repr` and `str` functions:

```py
>>> repr('hack')        # Returns a developer-readable, i.e. "as-code form" string `repr`esentation of an object
"'hack'"

>>> str('hack')         # Returns a human-readable string `str`ing representation of an object
'hack'
```

##### Comparison Operators

```py
>>> 1 < 2
True

>>> 2.0 >= 1            # Mixed-type 1 converted to 1.0
True

>>> 2.0 == 2.0
True

>>> 2.0 != 2.0
False
```

###### Chained Comparisons

Python supports chaining multiple comparisons together to perform range tests:

```py
>>> X = 2
>>> Y = 4
>>> Z = 6

>>> X < Y < Z           # Chained comparison: X < Y and Y < Z
True
>>> X < Y and Y < Z
True

>>> X < Y > Z           # Same equivalence holds for false results
False
>>> X < Y and Y > Z
False

>>> 1 < 2 < 3.0 < 4     # Arbitrary chain lengths allowed
True
>>> 1 > 2 > 3.0 > 4
False

>>> 1 == 2 < 3                  # Same as: (1 == 2) and (2 < 3)
False
>>> True is False is True       # Same as: (True is False) and (False is True)
False
```

###### Floating-Point Equality

Floating-point numbers are not always equal to each other, even if they look like they should be. This is due to the way floating-point numbers are represented in binary, which can lead to small rounding errors.

```py
>>> 1.1 + 2.2 == 3.3        # Shouldn't this be True?
False   

>>> 1.1 + 2.2               # CLose to 3.3, but not exactly: limited precision
3.3000000000000003
```

To address this issue, either truncate, round, use floors, or call the `math.isclose()` function to compare floating-point numbers with a tolerance for small differences:

```py
>>> int(1.1 + 2.2) == int(3.3)                  # OK if convert: see also floor, trunc ahead
True

>>> round(1.1 + 2.2, 1) == round(3.3, 1)
True

>>> import math                                 
>>> math.isclose(1.1 + 2.2, 3.3)                # Within default-but-passable tolerances
True
```

##### Division Operators

Python has two division operators: `/` for true division and `//` for floor division.

- `X / Y`: Called *true* division. Always keeps remainders in floating-point results, regardless of types.
- `X // Y`: Called *floor* division. Discards the decimal digits in the result, returning truncated floating-point for floats.
- `X % Y`: Called *modulus*, which returns the remainder of the division.

```py
>>> 10 / 4                  # True division: keeps remainders
2.5

>>> 10 / 4.0                # Same with float: keeps remainders
2.5

>>> 10 // 4                 # Floor division: drops remainder
2

>>> 10 // 4.0               # Same with float: drops remainder
2.0

>>> int(10 // 4.0)          # To ensure an integer result, wrap the expression into an `int` to convert
2

>>> 10 % 3, 10 % 3.0        # Remainder of division: (3 * 3) + 1
(1, 1.0)

>>> divmod(10, 3)           # Both parts of division in a tuple
(3, 1)
```

###### Floor versus truncation

The `//` operator is informally called *truncating* division, but it's more accurate to refer to it as *floor* division because it always rounds down to the nearest whole number, even for negative numbers:

```py
>>> import math
>>> math.floor(2.5)             # Closest number below value
2

>>> math.floor(-2.5)            # But not truncation for negative!
-3

>>> math.trunc(2.5)             # Truncate fractional part (toward zero)
2

>>> math.trunc(-2.5)            # And is truncation for negative
-2
```


```py
>>> 5 / 2, 5 / -2               # True division: keeps remainders
(2.5, -2.5)

>>> 5 // 2, 5 // -2             # Truncates to floor: rounds to the first lower integer
(2, -3)

>>> 5 / 2.0, 5 / -2.0           # Ditto for floats
(2.5, -2.5)

>>> 5 // 2.0, 5 // -2.0         # Though result is a float, too
(2.0, -3.0)
```

```py
>>> import math                 
>>> 5 / -2                      # Keep remainder
-2.5

>>> 5 // -2                     # Floor below result
-3

>>> math.trunc(5 / -2)          # Truncate instead of floor (same as int())
-2
```

##### Integer Precision

Python integers suppport unlimited size:

```py
>>> 99999999999999999999999999999999999999999999999999999999 + 1
100000000000000000000000000000000000000000000000000000000

>>> 2 ** 269
948568795032094272909893509191171341133987714380927500611236528192824358010355712

>>> 2 ** 1000000
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    2 ** 1000000
    ~~^^~~~~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

##### Complex Numbers

Complex numbers are a distinct core object type in Python.

```py
>>> 1j * 1J
(-1+0j)

>>> 2 + 1j * 3
(2+3j)

>>> (2 + 1j) * 3
(6+3j)
```

##### Hex, Octal, and Binary

```py
>>> 0x01, 0x10, 0xFF            # Hex literals: based 16, digits 0-9, A-F
(1, 16, 255)

>>> 0o1, 0o20, 0o377            # Octal literals: base 8, digits 0-7
(1, 16, 255)

>>> 0b1, 0b10000, 0b11111111    # Binary literals: base 2, digits 0-1
(1, 16, 255)
```

Python prints in decimal by default, but you can use the built-in `hex`, `oct`, and `bin` functions to convert numbers to their string representations in other bases:

```py
>>> oct(64), hex(64), bin(64)               # Numbers => digit strings
('0o100', '0x40', '0b1000000')
```

```py
>>> 64, 0o100, 0x40, 0b1000000              # Digits => numbers in scripts and strings
(64, 64, 64, 64)

>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2)
(64, 64, 64, 64)

>>> int('0x40', 16), int('0b1000000', 2)    # Literal forms supported, too
(64, 64)
```

The `eval` function can convert digit strings to numbers because it treats strings as though they were Python code:

```py
>>> eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')
(64, 64, 64, 64)
```

You can convert integers to base-specific strings with any of Python's three string-formatting tools:

```py
>>> '%o, %x, %#X' % (64, 255, 255)                          # Old-style formatting using `%` operator
'100, ff, 0XFF'

>>> '{:o}, {:b}, {:x}, {:#X}'.format(64, 64, 255, 255)      # New-style formatting using `str.format()`
'100, 1000000, ff, 0XFF'

>>> f'{64:o}, {64:b}, {255:x}, {255:#X}'                    # F-string formatting (latest and greatest)
'100, 1000000, ff, 0XFF'
```

**Note:** `#X` in these examples adds a base prefix and uses uppercase letters for hex digits.

In the following code, you can avoid repeating the same value by using named arguments or assignment expressions:

```py
>>> '%(i)o, %(j)x, %(j)#X' % dict(i=64, j=255)              # Old-style formatting with named arguments
'100, ff, 0XFF'

>>> '{0:o}, {0:b}, {1:x}, {1:#X}'.format(64, 255)           # New-style formatting with positional arguments
'100, 1000000, ff, 0XFF'

>>> f'{(i:=64):o}, {i:b}, {(i:=255):x}, {i:#X}'             # F-string formatting with assignment expressions
'100, 1000000, ff, 0XFF'
```

**Note:** The `:=` operator is the Walrus operator and allows you to assign a value to a variable as part of an expression.

Other-base literals and converters support *arbitrarily* large integers:

```py
>>> X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> X
87112285931760246646623899502532662132735
>>> oct(X)
'0o1777777777777777777777777777777777777777777777'
>>> bin(X)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
```

##### Bitwise Operators

Python suports most of the numeric expressions available in C. This includes operators that treat integers as strings of binary bit. This comes in hand when dealing with low-level data like network packets, serial ports, or packed binary data produced for a C program.

```py
>>> x = 1               # 1 in decimal is 0001 in binary

>>> x << 2              # Shift left by 2 bits: 0100
4

>>> x | 3               # Bitwise OR: (either bit=1): 0001 | 0011
3

>>> x & 3               # Bitwise AND: (both bits=1): 0001 & 0011
1
```

One useful area in Python is the ability to inspect numbers by bit-strings:

```py
>>> X = 0b0001          # A 4-bit binary number

>>> X << 2              # Shift left by 2 bits: 0100
4

>>> bin(X << 2)         # Binary digits string
'0b100'

>>> bin(X | 0b011)      # Bitwise OR: (either bit=1): 0001 | 0011
'0b11'

>>> bin(X & 0b11)       # Bitwise AND: (both bits=1): 0001 & 0011
'0b1'
```

This is also available for values that begin life as hex literals or undergo base conversions:

```py
>>> X = 0xFF                    # Hex literals

>>> bin(X)                      
'0b11111111'

>>> X ^ 0b10101010              # Bitwise XOR: (either bit=1, but not both): 11111111 ^ 10101010
85

>>> bin(X ^ 0b10101010)         # Binary digits string
'0b1010101'

>>> int('01010101', 2)          # Digits=>number: string to int per base
85

>>> hex(85)                     # Number=>digits: hex digit string
'0x55'
```

Python integers come with a `bit_length()` method, which allows you to query the number of bits required to represent the number's value in binary:

```py
>>> X = 99

>>> bin(X), X.bit_length(), len(bin(X)) - 2             # Binary digits string, bit length, and length minus '0b' prefix
('0b1100011', 7, 7)

>>> bin(256), (256).bit_length(), len(bin(256)) - 2    
('0b100000000', 9, 9)
```

##### Underscore Separators in Numbers

Numeric literals can use underscores to improve readability, especially for large numbers. 

```py
>>> 9999999999999 == 9_999_999_999_999                      # Decimal: thousands
True

>>> 0xFFFFFFFF == 0xFF_FF_FF_FF                             # Hex: 8-bit bytes
True

>>> 0o777777777777 == 0o777_777_777_777                     # Octal: 9 bits each
True

>>> 0b1111111111111111 == 0b1111_1111_1111_1111             # Binary: 4-bit nibbles
True

>>> 3.141592653589793 == 3.141_592_653_589_793              # Float: decimal digits
True

>>> 123456789.123456789 == 123_456_789.123_456_789          # Float: both sides
True
```

The underscores are just for show. Numbers lose their underscores once read.

You can add back comma and underscore separators with the *string-formatting* method and f-strings:

```py
>>> x = 9_999_998               # Underscore separators in numbers
>>> x                           # Dropped when read: not in displays
9999998                         
>>> x + 1                       # Ditto for derived computation results
9999999

>>> f'{x:,} and {x:_}'          # Formatting adds separators, but just for show
'9,999,998 and 9_999_998'
```

Python doesn't do any sanity checks on underscores, except for disallowing leading, trailing, and multiple-appearance uses. The underscores are just digit "spacers" that can be used&mdash;and misused&mdash; arbitrarily:

```py
>>> 99_9                                # No position-error checking
999

>>> 1_23_456_7890                       
1234567890

>>> _9                                                     
NameError: name '_9' is not defined. Did you mean: '_'?

>>> 9_
SyntaxError: invalid decimal literal

>>> 9_9__9
SyntaxError: invalid decimal literal

>>> 9_9_9                               # Syntax oddities checked, semantics not
999

>>> hex(0xf_ff_fff_f_f)                 # Python doesn't retain your "_"s
'0xffffffff'
``` 

Also note that comma's can't be used in numeric literals, as comma's are reserved for tuples:

```py
>>> 12_345_678
12345678

>>> 42,345,678
(42, 345, 678)
```

Underscores are helpful for input for string-to-number conversions:

```py
>>> int('1_234_567')
1234567

>>> eval('1_234_567')
1234567

>>> float('1_2_34.567_8_90')
1234.56789
```

##### Other Built-In Numeric Tools

Python has built-in functions and standard-library modules for numeric processing:

```py
>>> import math
>>> math.pi, math.e                         # Common constants
(3.141592653589793, 2.718281828459045)

>>> math.sin(2 * math.pi / 180)             # Sine, tangent, cosine
0.03489949670250097

>>> math.sqrt(144), math.sqrt(2)            # Square root
(12.0, 1.4142135623730951)

>>> pow(2, 4), 2 ** 4,  2.0 ** 4.0          # Exponentiation
(16, 16, 16.0)

>>> abs(-62.0), sum((1, 2, 3, 4))           # Absolute value, summation
(62.0, 10)

>>> min(3, 1, 2, 4), max(3, 1, 2, 4)        # Minimum, maximum
(1, 4)
```

There are also multiple ways to drop the decimal digits of floating-point numbers:

```py
>>> math.floor(2.567), math.floor(-2.567)               # Floor: next-lower integer
(2, -3)

>>> math.trunc(2.567), math.trunc(-2.567)               # Truncation: drop digits
(2, -2)

>>> int(2.567), int(-2.567)                             # Truncate: alternative
(2, -2)

>>> round(2.567), round(2.567, 2), round(2567, -3)      # Round to digits (+/-)
(3, 2.57, 3000)

>>> '%.1f' % 2.567, '{0:.2f}'.format(2.567)             # Format display
('2.6', '2.57')
```

`round()` rounds and drops. String formatting produces a string, not a number:

```py
>>> (1 / 3.0), round(1 / 3.0, 2), f'{(1 / 3.0):.2f}'
(0.3333333333333333, 0.33, '0.33')
```

There are different ways to compute square roots in Python: using a module function, an expression, or a built-in function:

```py
>>> import math
>>> math.sqrt(144)      # Module
12.0

>>> 144 ** .5           # Expression
12.0

>>> pow(144, .5)        # Built-in function
12.0
```

The `statistics` and `random` modules provide additional numeric tools:

```py
>>> import statistics
>>> statistics.mean([1, 2, 4, 5, 7])
3.8

>>> statistics.median([1, 2, 4, 5, 7])
4

>>> import random
>>> random.random()
0.3397783973044639

>>> random.random()
0.9632919797894054

>>> random.randint(1, 10)
10

>>> random.randint(1, 10)
5
```

The `random` module can also choose an item at random from a sequence and shuffle a list of items randomly:

```py
>>> random.choice(['Pizza', 'Tacos', 'Tikka', 'Lasagna'])
'Pizza'

>>> random.choice(['Pizza', 'Tacos', 'Tikka', 'Lasagna'])
'Tacos'

>>> suits = ['hearts', 'clubs', 'diamonds', 'spades']  

>>> random.shuffle(suits)
>>> suits
['clubs', 'hearts', 'spades', 'diamonds']

>>> random.shuffle(suits)
>>> suits
['hearts', 'spades', 'diamonds', 'clubs']
```

#### Other Numeric Objects
