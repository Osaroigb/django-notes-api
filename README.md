# Django Notes API

The Django Notes API is a simple, RESTful API built with Django and Django REST Framework (DRF) for creating, reading, updating, and deleting notes. Each note consists of a title and content. This API uses PostgreSQL as its database backend.

## Features

- CRUD operations for notes
- RESTful endpoints
- PostgreSQL database integration
- Custom error response formats
- Input validation

## Getting Started

### Prerequisites

Before you begin, ensure you have installed:

- Python 3.8 or later
- pip (Python package manager)
- Virtualenv (optional, but recommended for creating isolated Python environments)
- PostgreSQL

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/django-notes-api.git
   cd django-notes-api
   ```

2. **Set Up a Virtual Environment (Optional)**

   Create a new virtual environment:

   ```bash
   python -m venv env
   ```

   Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```

3. **Install Dependencies**

   Install all the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**

   - Create a PostgreSQL database for the project.
   - Note the database host, port, name, user, and password.

5. **Update Settings**

To configure your database settings securely, we use environment variables. You'll find a file named `.env.example` in the project root. This file contains template environment variable definitions for your project's configuration, including database connection details.

6. **Copy `.env.example` to `.env`**

   First, create a copy of the `.env.example` file and name it `.env`. This file will be used to set your environment variables. The command you use to copy this file depends on your operating system:

   - On macOS/Linux:
     ```bash
     cp .env.example .env
     ```
   - On Windows (Command Prompt):
     ```cmd
     copy .env.example .env
     ```
   - On Windows (PowerShell):
     ```powershell
     Copy-Item .env.example -Destination .env
     ```

7. **Update `.env` File**:

   Open the newly created `.env` file in your preferred text editor. You will see several lines that look like this:

   ```plaintext
   POSTGRES_DB_NAME=your_database_name
   POSTGRES_DB_USER=your_database_user
   POSTGRES_DB_PASSWORD=your_database_password
   POSTGRES_DB_HOST=localhost
   POSTGRES_DB_PORT=5432
   ```

   Replace `your_database_name`, `your_database_user`, `your_database_password`, `localhost`, and `5432` with your actual PostgreSQL database name, user, password, host, and port, respectively.

8. **Run Migrations**

   Apply the migrations to create the database schema:

   ```bash
   cd notes_project
   python manage.py makemigrations
   python manage.py migrate
   ```

### Running the API Locally

1. **Start the Development Server**

   Run the following command to start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/v1/api`.

2. **Accessing the API Endpoints**

   Use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to interact with the API. Here are some example endpoints:

   - Create a new note: `POST /notes/`
   - Retrieve all notes: `GET /notes/`
   - Retrieve a single note by ID: `GET /notes/<note_id>/`
   - Update a note: `PUT /notes/<note_id>/`
   - Delete a note: `DELETE /notes/<note_id>/`

## Customization

Refer to the Django and Django REST Framework documentation for further customization and advanced features such as pagination, filtering, and authentication.

## License

This project is licensed under the Mozilla Public License - see the [LICENSE.md](LICENSE.md) file for details.