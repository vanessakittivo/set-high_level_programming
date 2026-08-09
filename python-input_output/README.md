# Python - Input/Output

This project covers Python input and output operations, file handling, JSON serialization and deserialization, object persistence, and basic data processing.

## Learning Objectives

By completing these tasks, I learned how to:

- Open, read, and write files in Python
- Use the `with` statement to work with files
- Read files line by line
- Write strings to files
- Append text to files
- Serialize Python objects into JSON
- Deserialize JSON data back into Python objects
- Convert Python classes into dictionary representations
- Save and reload objects using JSON
- Build Pascal's Triangle
- Process data from standard input
- Calculate statistics from log data

## Tasks

### 0. Read File

Write a function that reads a text file and prints its contents to standard output.

File:

`0-read_file.py`

### 1. Write to a File

Write a function that writes a string to a text file and returns the number of characters written.

File:

`1-write_file.py`

### 2. Append to a File

Write a function that appends a string to the end of a text file and returns the number of characters added.

File:

`2-append_write.py`

### 3. To JSON String

Write a function that returns the JSON representation of an object.

File:

`3-to_json_string.py`

### 4. From JSON String

Write a function that returns the Python representation of a JSON string.

File:

`4-from_json_string.py`

### 5. Save Object to a File

Write a function that writes an object to a text file using JSON representation.

File:

`5-save_to_json_file.py`

### 6. Load Object from a File

Write a function that creates an object from a JSON file.

File:

`6-load_from_json_file.py`

### 7. Add All Arguments

Write a script that adds all arguments passed to the command line and prints the result.

File:

`7-add_item.py`

### 8. Class to JSON

Write a function that returns the dictionary representation of an object.

File:

`8-class_to_json.py`

### 9. Student to JSON

Create a `Student` class with a method that returns its dictionary representation.

File:

`9-student.py`

### 10. Student to JSON with Filter

Update the `Student` class so that selected attributes can be returned using the `to_json()` method.

File:

`10-student.py`

### 11. Student to Disk and Reload

Update the `Student` class with a `reload_from_json()` method that replaces its attributes using a dictionary.

File:

`11-student.py`

### 12. Pascal's Triangle

Create a function that generates Pascal's Triangle for a given number of rows.

File:

`12-pascal_triangle.py`

### 13. Search and Update

Write a function that inserts a line of text after every line containing a specified string.

File:

`100-append_after.py`

### 14. Log Parsing

Create a script that reads log information from standard input and calculates:

- Total file size
- Number of occurrences of each status code
- Statistics every 10 lines
- Final statistics after a keyboard interruption

File:

`101-stats.py`

## Requirements

- Python 3
- PEP 8 style
- Code should be executable
- Functions and classes should follow the required prototypes
- No unnecessary imports
- JSON is used for serialization and deserialization where required

## Repository

GitHub repository:

`set-high_level_programming`

Project directory:

`python-input_output`