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
