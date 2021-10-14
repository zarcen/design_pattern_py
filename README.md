# Design Pattern using python implementation

## Introduction

### Prerequisite
* `python3 (python-3.9.5)`
* `pip/pip3 (pip-20.0.2)`
* `pytest (pytest-6.2.4)`

This repo demonstrates various design patterns implementation in python.
The goal is to maintain quick templates as these patterns would be used over and over during development :neutral_face:.

### Why python :thinking:?
Well, most design patterns are naturally derived from OOP languages like `Java` or `C#`.
There are tons of samples already when there's a need to bring up things from scratch with `Java` by applying certain pattern.
On the other hand, not so common for `python`.

### File Layout
For each pattern, it is structured as follows. \
**Note**: It is simply to be a `package` by putting an empty `__init__.py` 
```bash
pattern_foo/
    __init__.py               # needed to be treated as a pacakge
    pattern_foo_cxt1_abc.py   # "_abc" suffix as abstract class
    pattern_foo_cxt2_abc.py
    ...
    tests/
        __init__.py           # needed to be treated as a pacakge
        test_pattern.py
```

To run the test for a pattern:
```bash
$ pytest <pattern_name>
```

# Quick Pattern Links
* [Strategy Pattern](#strategy-pattern)
* [Observer Pattern](#observer-pattern)
* [Command Pattern](#command-pattern)

## SOLID Principles of OO Design

* **S**ingle respoinsibilie

    A class should have only **single one** responsibility

* **O**pen-closed

    A class should be **open** to extension, usually by _inheritance_.
    But **close** to modification.

* **L**iskov substitution

    Subclasses should be able to stand in for their parents in a program without breaking anything

* **I**nterface segregation

    Many specific interfaces are better than one do-it-all interface.
    (In python, using abstract base classes combined with multiple inheritance to achieve this)

* **D**ependency inversion

    Program toward abstrations not implementations.

## Abstraction Base Class Definition
Sadly, [PEP8](https://www.python.org/dev/peps/pep-0008/) doesn't have naming convention for `abc` (Abstract Base Class). Here, just use `I` prefix as the notation like other languages like `C++` or `Java`

According to module [`abc`](https://docs.python.org/3/library/abc.html),
simply inheriting from `abc.ABC` is the recommended way to define a ABC.

```python
from abc import ABC

class IFoo(ABC):
    """Abstract Base Class Definition"""

    # Define a abstract method
    @abc.abstractmethod
    def do_something(self, val):
        """Required method"""

    # Define a abstract property
    @abc.abstractproperty
    def some_property(self):
        """Required property"""

```

## Concrete Class Implementation
Derived class inherits the `ABC`. Like `C++`, python supports multiple inheritance.\
Say, Foo implements two `ABC`s: `IFoo` and `IBar`

```python
class Foo(IFoo, IBar):
    """Implementation of IFoo and IBar"""

    def __init__(self, val=None):
        self._val = val

    def do_something(self, val):
        """Implementation of abstract method"""
        self._val += 10
    
    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._val
    
    @property
    def bar_property(self):
        return self._bar

```

## Strategy Pattern

* Classification: Behavioral
* Family of algorithms
* Encapsulate each one
* Make them **_interchangeable_**
* Algorithms vary independently
* Also know as: *Policy Pattern*

## Observer Pattern

* Classification: Behavioral
* One to many relationship
* Between a set of objects
* When the state of one changes…
* Its dependents are notified
* Also know as: *Dependents pattern* or *Publish-Subscribe pattern*
* Used a lot in GUI
* In **MVC** pattern: Model = `Subject`, Viewer = `Observer`

## Command Pattern

* Classification: Behavioral
* Encapsulate a request as an object
* Parameterize objects
* Queues and log operations
* Undoable operations and macros
* Also know as: *Action pattern* or *Transaction pattern*
* Useful for command line programs and **menu** like applications (each menu item is like a command)
* Easy to provide `validation` and `undo` for a command