# FastAPI Project

This is a simple FastAPI project that demonstrates user authentication and item management. It uses a MySQL database to store user and item data.

## Project Structure

- `app/`: This directory contains the main application code.
  - `main.py`: The entry point of the FastAPI application. It initializes the database and includes the API routers.
  - `database.py`: Handles the database connection and session management.
  - `auth.py`: Contains the API endpoints for user authentication (e.g., login, registration).
  - `users.py`: Contains the API endpoints for user-related operations.
  - `items.py`: Contains the API endpoints for item-related operations.
  - `crud.py`: Contains the CRUD (Create, Read, Update, Delete) operations for the database.
  - `schemas.py`: Defines the Pydantic schemas for data validation and serialization.
  - `security.py`: Handles security-related tasks, such as password hashing and token generation.
  - `dependencies.py`: Defines dependencies for the application, such as getting the current user.
- `requirements.txt`: Lists the Python dependencies for the project.
- `.gitignore`: Specifies the files and directories that should be ignored by Git.

## Getting Started

### Prerequisites

- Python 3.7+
- MySQL

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-name>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Make sure you have a MySQL server running.
2. Create a database for the project.
3. Update the database connection details in `app/database.py`.

### Running the Application

Once you have set up the database and installed the dependencies, you can run the application using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.
