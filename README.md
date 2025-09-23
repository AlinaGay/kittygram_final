#  Cats API

A Django REST Framework project that provides an API for managing cats and their achievements.
Users can create, view, update, and delete information about cats, upload their photos, and assign achievements.

## Features

- Cats management: Full CRUD operations for cat profiles.
- Achievements: Create and manage achievements that cats can earn.
- Owner assignment: The owner of a cat is automatically set to the currently authenticated user.
- Pagination: Built-in pagination for cat listings.
- Custom fields:
-- Hex color codes are automatically converted to human-readable color names.
-- Base64-encoded image uploads supported out of the box.
- Automatic age calculation: The API returns the cat’s age calculated from its birth year.

## Tech Stack

- Python 3
- Django
- Django REST Framework
- webcolors — for converting hex color codes to names.
- PostgreSQL or any other database supported by Django.

## How to run the project:

Clone the repository and navigate into it in the command line:
```
git clone https://github.com/AlinaGay/kittygram_final.git
cd kittygram_backend
```
Create and activate a virtual environment:
* If you have Linux/macOS
    ```
    source env/bin/activate
    ```
* If you have windows
    ```
    source env/scripts/activate
    ```
Update pip:
```
python3 -m pip install --upgrade pip
```
Apply migrations:
```
python3 manage.py migrate
```
Start the project:
```
python3 manage.py runserver
```
## Author

[AlinaGay](https://github.com/AlinaGay)
| Backend Developer • Python Engineer |
