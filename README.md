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

2. Replace the DATABASE_URL in `app/database.py` with your PostgreSQL credentials.

### Installation

1. Clone the repository:
   `git clone https://github.com/mouadlasri/url-shortener-fastpi.git`
   `cd url-shortener-fastpi`

2. Create a vritual environment and activate it
   `python -m venv venv`
   `source venv/bin/activate`
   On Windows use `venv\Scripts\activate`

3. Install the required packages:
   `pip install -r requirements.txt`

4. Run the database migrations
   alembic upgrade head

### Running the application

To start teh application, run:
`python run.py`
The API will be available at http://localhost:8000.

**API Endpoints**
POST /shorten: Create a shortened URL
GET /{short_key}: Redirect to the original URL
GET /stats/{short_key}: Get statistics for a shortened URL

### Running Tests

1. Create a test database

2. Replace the TEST_DATABASE_URL in tests/test_main.py with your PostgreSQL credentials.

3. Run the test:
