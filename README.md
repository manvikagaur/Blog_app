# Blog App Admin

This is a Django project for managing a blog application with REST API functionality. It supports user authentication, creating, updating, retrieving, and deleting posts and comments. The project uses Django REST Framework and JWT for token-based authentication.

## Features

- User authentication with JWT
- CRUD operations for posts
- List and create operations for comments
- Token-based authentication for secured API access

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/manvikagaur/blog_app.git
   cd blog_app
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Swagger-UI 

    To test open http://127.0.0.1:8000/api/schema/swagger-ui/


## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```


