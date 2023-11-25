# moviematrix

This project was made to search for movies and get information.
The user can search by movie name and category.
Movies come from the TMDB database via an API.

## Technology and requirements
This project is based on:

Python 3.11.2

Django4.2.6

MYSQL


## Installation

1. Clone the repository:

git clone https://github.com/your-username/moviematrix.git
   cd moviematrix

2. Install the project dependencies:

   pip install -r requirements.txt

3. Create a virtual environment and install dependencies:

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

4. Copy the example environment file:

cp .env.example .env

5. Database Setup

Ensure MySQL is installed and running.

Create a MySQL database named moviematrix.

Update the database configuration in .env with your MySQL credentials

6. Start the development server

python manage.py runserver


## API reference

This app uses The Movie Database(TMDB) API to fetch data.








