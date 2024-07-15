# url-shortener-fastapi

A URL shortenner implemented using FastAPI

## Installation

1. Clone the repository:
   git clone https://github.com/mouadlasri/url-shortener-fastpi.git
   cd url-shortener-fastapi

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate

On Windows, use: venv\Scripts\activate
On Mac, use: source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

## Running the app

to run the application, use the following command: python run.py
The api will be available at `http://localhost:8000`

## API Endpoints

- POST /shorten: Create a shortened URL
- GET /{short_key}: Redirect to the original UR

## Setting up the database

This project uses PostgreSQL:

1. Update the `DATABASE_URL` in `app/database.py` with your PostgreSQL credentials.
2. Run Alembic migrations to create the necessary tables:
   2.1. alembic upgrade head

## Project Structure

The proejct is structured as follows:

fastapi-url-shortener/
│
├── app/ <br />
│ ├── init.py
│ ├── main.py # Main FastAPI application
│ ├── database.py # Database connection and session management
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas for request/response models
│ └── utils.py # Utility functions
│
├── alembic/ # Database migration scripts and configuration
│ ├── versions/
│ └── env.py
│
├── alembic.ini # Alembic configuration file
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── run.py # Script to run the FastAPI application
