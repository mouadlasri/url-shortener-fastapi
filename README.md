# FastAPI URL Shortener

A scalable URL shortening service built with FastAPI and PostgreSQL.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting up the Database](#setting-up-the-database)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [API Documentation](#api-documentation)
- [Running Tests](#running-tests)
- [Why PostgreSQL?](#why-postgresql)

## Project Overview

This URL shortener service provides functionality to shorten long URLs into more manageable, shorter versions. It includes features like URL expiration and click tracking.

## Features

- Shorten long URLs to unique short keys
- Redirect short URLs to original long URLs
- Set expiration dates for URLs
- Track click statistics for each shortened URL

## Technology Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic**
- **Pydantic**

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL

### Setting up the Database

1. Install PostgreSQL and create a new database:

`CREATE DATABASE url_shortener;`

2. Replace the `DATABASE_URL` in `app/database.py` with your PostgreSQL credentials.

### Installation

1. Clone the repository:
   `git clone https://github.com/mouadlasri/url-shortener-fastpi.git`
   <br />
   `cd url-shortener-fastpi`

2. Create a vritual environment and activate it
   <br />
   `python -m venv venv`
   <br />
   On mac use `source venv/bin/activate`
   <br />
   On Windows use `venv\Scripts\activate`

3. Install the required packages:
   <br />
   `pip install -r requirements.txt`

4. Run the database migrations
   <br />
   `alembic upgrade head`

### Running the application

To start teh application, run:
<br />
`python run.py`
<br />
The API will be available at http://localhost:8000.

**API Endpoints**
<br />
POST /shorten: Create a shortened URL
<br />
GET /{short_key}: Redirect to the original URL
<br />
GET /stats/{short_key}: Get statistics for a shortened URL

### Running Tests

1. Create a test database

2. Replace the TEST_DATABASE_URL in tests/test_main.py with your PostgreSQL credentials.

3. Run the test:

## API Documentation

FastAPI provides automatic interactive API documentation (Swagger UI) for your API endpoints.

To access the Swagger documentation:

1. Start the application:
   `python run.py`

2. Open a browser and go to <br />
   `http://localhost:8000/docs`
3. Access the documentation through the Swagger UI at: <br />
   `http://localhost:8000/docs`
