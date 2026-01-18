# FastAPI & PostgreSQL Inventory Manager
A robust RESTful API built with FastAPI and SQLAlchemy to manage a product inventory system. This project serves as a comprehensive backend practice for integrating a Python web framework with a PostgreSQL database.

🛠️ Tech Stack
Framework: FastAPI

ORM: SQLAlchemy

Database: PostgreSQL

Data Validation: Pydantic

Database Driver: psycopg2

🏗️ Architecture
The project is structured to separate concerns between data models, API logic, and database configuration:

database.py: Establishes the engine connection and session factory.

database_model.py: Defines the SQLAlchemy ORM models (Database Schema).

models.py: Defines Pydantic schemas for request/response data validation.

main.py: Contains the API endpoints and dependency injection logic.

🌟 Key Features
Automatic Table Creation: Uses SQLAlchemy's Base.metadata.create_all to automatically generate the product table in PostgreSQL.

Dependency Injection: Implements a get_db generator to ensure database sessions are opened and closed safely for every request.

CRUD Operations:

Create: Add new items to the inventory.

Read: Fetch all products or a specific item by ID.

Update: Modify existing product details (name, price, quantity).

Delete: Remove products from the database.

Seed Data: Automatically populates the database with initial items if the table is empty upon startup.

The code is divided into two parts.

Part one focus on performing operations using a simple List. 
Part two focus on performing operations using Database. 
