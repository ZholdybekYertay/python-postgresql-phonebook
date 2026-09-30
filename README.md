# PostgreSQL PhoneBook

A command-line phone book application built with Python and PostgreSQL.

## Features

- Add, update and delete contacts
- Search contacts by different fields
- Organize contacts into groups
- Import contact data from CSV and JSON files
- Store data in PostgreSQL
- Create the database schema and stored procedures from SQL files
- Keep database credentials in environment variables

## Technologies

- Python
- PostgreSQL
- psycopg2
- python-dotenv
- SQL stored procedures

## Project Structure

- `phonebook.py` - application logic and command-line menu
- `connect.py` - PostgreSQL connection
- `config.py` - environment configuration
- `schema.sql` - database tables
- `procedures.sql` - PostgreSQL procedures
- `.env.example` - example environment variables

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ZholdybekYertay/python-postgresql-phonebook.git
cd python-postgresql-phonebook
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and enter your PostgreSQL credentials.

5. Run the application:

```bash
python phonebook.py
```

## Security

The .env file and virtual environment are excluded from Git. Do not commit CSV or JSON exports containing personal contact data.