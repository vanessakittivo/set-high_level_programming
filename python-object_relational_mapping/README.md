# Python - Object Relational Mapping

## Description

This project introduces Object Relational Mapping (ORM) in Python using MySQLdb and SQLAlchemy.

The tasks cover connecting Python applications to MySQL databases, executing SQL queries safely, and using SQLAlchemy to map Python classes to database tables.

## Learning Objectives

At the end of this project, I should be able to:

- Connect to a MySQL database from Python using `MySQLdb`
- Execute SQL queries from Python
- Retrieve and filter database records
- Protect SQL queries from SQL injection
- Use SQLAlchemy to interact with databases
- Define database models using SQLAlchemy
- Create tables from Python classes
- Query database objects using SQLAlchemy
- Add, update, and delete database records
- Create relationships between database models
- Use relationships to access related objects

## Requirements

- Python 3
- MySQL
- MySQLdb
- SQLAlchemy
- Ubuntu/Linux environment

## Project Files

| File | Description |
|---|---|
| `0-select_states.py` | Lists all states |
| `1-filter_states.py` | Lists states whose names start with `N` |
| `2-my_filter_states.py` | Filters states by user input |
| `3-my_safe_filter_states.py` | Safely filters states without SQL injection |
| `4-cities_by_state.py` | Lists all cities with their states |
| `5-filter_cities.py` | Lists cities belonging to a specified state |
| `model_state.py` | Defines the SQLAlchemy `State` model |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Retrieves the first `State` |
| `9-model_state_filter_a.py` | Finds states containing `a` |
| `10-model_state_my_get.py` | Retrieves a state by name |
| `11-model_state_insert.py` | Adds a new state |
| `12-model_state_update_id_2.py` | Updates state ID 2 |
| `13-model_state_delete_a.py` | Deletes states containing `a` |
| `model_city.py` | Defines the SQLAlchemy `City` model |
| `14-model_city_fetch_by_state.py` | Lists cities with their states |
| `relationship_state.py` | Defines the `State` relationship |
| `relationship_city.py` | Defines the `City` relationship |
| `100-relationship_states_cities.py` | Creates a state and related city |
| `101-relationship_states_cities_list.py` | Lists states and their cities |
| `102-relationship_cities_states_list.py` | Lists cities and their states |

## Key Concepts

### MySQLdb

The first tasks use `MySQLdb` to connect directly to MySQL and execute SQL queries.

### SQL Injection

The project demonstrates the difference between constructing SQL queries with user input and using parameterized queries to prevent SQL injection.

### SQLAlchemy ORM

Later tasks use SQLAlchemy's ORM to represent database tables as Python classes.

