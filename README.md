# Moviematrix


![image](https://github.com/IngaFom/moviematrix/assets/144582845/4a45d56c-cecc-430c-a821-6e0d3381e297)


Moviematrix is our SDA Python course final project. 

This project was made to search for movies and get information.
The user can search by movie name and category.
Movies come from the TMDB database via an API.

## Technology
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


The fetch_api function is a utility in the moviem project that simplifies making requests to The Movie Database (TMDb) API.

It is responsible for constructing the API endpoint URL based on the provided request_type and optional parameters,
making the API request, and handling potential errors.

API_KEY is in the settings.

## Views

In this project we use function_based views.

## Testing

In project you can test our API_KEY, register, login and search_view and couple more.

To test code go tests.py and run   python manage.py test moviem.tests.Tests




## Credits

This project was made as a collaboration by

Tõnu Jõks

Inga Fomitsjova

Kevin Saare

Denis Kabanov








