# Notes from "Learning Python" by Mark Lutz

<img src='images/20250409025850.png' width='250'/>

<details>
<summary>Book Resources</summary>

- [Book Code](https://learning-python.com/LP6E-code)
- [Python Documentation](https://docs.python.org/3/)

</details>

## Objects and Operations

### The Python Conceptual Hierarchy
1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

#### Python's Core Object Types

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

