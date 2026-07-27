# Python - Inheritance

This project is part of the Higher-level programming curriculum.

This project introduces inheritance in Python and explores how classes can inherit attributes and methods from other classes.

## Learning Objectives

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When an instance can have new attributes
* How to inherit a class from another class
* How to define a class with multiple base classes
* What is the default class every class inherits from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by inheritance
* How Python finds the right function or method to execute
* How to use the built-in `isinstance`, `issubclass`, `type` and `super` functions

## Requirements

* All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files end with a new line
* The first line of all Python files is exactly `#!/usr/bin/python3`
* Code uses pycodestyle version 2.8.*
* All files are executable
* The length of files is tested using `wc`

## Project Files

### Task 0 - Lookup

**File:** `0-lookup.py`

Defines a function that returns a list of available attributes and methods of an object.

### Task 1 - My List

**File:** `1-my_list.py`

Defines a `MyList` class that inherits from Python's built-in `list` class.

The class includes a `print_sorted` method that prints the list in ascending sorted order without modifying the original list.

### Task 2 - Exact Same Object

**File:** `2-is_same_class.py`

Defines a function that checks whether an object is exactly an instance of a specified class.

### Task 3 - Same Class or Inherit From

**File:** `3-is_kind_of_class.py`

Defines a function that checks whether an object is an instance of a specified class or an instance of a class that inherited from it.

### Task 4 - Only Sub Class Of

**File:** `4-inherits_from.py`

Defines a function that checks whether an object is an instance of a class that inherited from a specified class.

### Task 5 - Geometry Module

**File:** `5-base_geometry.py`

Defines an empty `BaseGeometry` class.

### Task 6 - Improve Geometry

**File:** `6-base_geometry.py`

Defines a `BaseGeometry` class with an `area` method that raises an exception because the method is not implemented.

### Task 7 - Integer Validator

**File:** `7-base_geometry.py`

Adds an `integer_validator` method to `BaseGeometry`.

The method validates that a value is an integer greater than zero.

### Task 8 - Rectangle

**File:** `8-rectangle.py`

Defines a `Rectangle` class that inherits from `BaseGeometry`.

The class validates its width and height and stores them as private attributes.

### Task 9 - Full Rectangle

**File:** `9-rectangle.py`

Extends the `Rectangle` class with:

* An `area` method
* A `__str__` method

### Task 10 - Square #1

**File:** `10-square.py`

Defines a `Square` class that inherits from `Rectangle`.

The square uses the same value for its width and height.

### Task 11 - Square #2

**File:** `11-square.py`

Extends the `Square` class with a custom `__str__` representation.

### Task 12 - My Integer

**File:** `100-my_int.py`

Defines a `MyInt` class that inherits from `int`.

The `==` and `!=` operators are inverted.

### Task 13 - Can I?

**File:** `101-add_attribute.py`

Defines a function that adds a new attribute to an object when the object allows it.

If the object cannot accept a new attribute, a `TypeError` is raised.

## Concepts Practiced

* Inheritance
* Superclass and subclass relationships
* Method overriding
* Built-in classes
* Private attributes
* Class validation
* `isinstance()`
* `issubclass()`
* `type()`
* `super()`
* Operator overriding


