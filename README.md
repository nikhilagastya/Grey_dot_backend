# Grey_dot_backend
**Task Management RESTful API**

This project is a simple RESTful API for managing tasks. It allows you to create, retrieve, update, and delete tasks. The tasks are stored in a SQLite database, and the API is implemented using Python and Flask.

**Project Structure:**

- `app.py`: The main entry point of the application. It sets up the Flask app and defines the API endpoints.
- `models.py`: Contains the `Task` class representing a task and the `TaskEncoder` class for JSON serialization of tasks.
- `services.py`: Handles the connection to the SQLite database and provides helper functions for executing SQL queries.
- `controllers.py`: Defines the functions that handle the API endpoints and interact with the database.
- `Requirements.txt`: Lists the Python dependencies required for the project.

**API Endpoints:**

- `GET /tasks`: Retrieves a paginated list of all tasks.
- `GET /tasks/<task_id>`: Retrieves a single task by its ID.
- `POST /tasks`: Creates a new task.
- `PUT /tasks/<task_id>`: Updates an existing task.
- `DELETE /tasks/<task_id>`: Deletes a task by its ID.

**Files and Their Functionality:**

- `app.py`:
  - Sets up the Flask app and initializes the routes.
  - Defines the API endpoints and their corresponding functions.

- `models.py`:
  - Defines the `Task` class representing a task.
  - Implements the `TaskEncoder` class for JSON serialization of tasks.

- `services.py`:
  - Establishes a connection to the SQLite database.
  - Provides helper functions for executing SQL queries.

- `controllers.py`:
  - Contains the functions that handle the API endpoints.
  - Implements the logic for creating, retrieving, updating, and deleting tasks.
  - Uses the database helper functions to interact with the SQLite database.

**Usage:**

To set up and run the project locally, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment:
   - For Windows: `.\env\Scripts\activate`
   - For Linux/Mac: `source env/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Create a SQLite database file named `tasks.db`.
6. Run the application: `python app.py`

The API will be accessible at `http://localhost:5000`.

**API Usage:**

- `GET /tasks`: Retrieves a paginated list of all tasks.
- `GET /tasks/<task_id>`: Retrieves a single task by its ID.
- `POST /tasks`: Creates a new task.
- `PUT /tasks/<task_id>`: Updates an existing task.
- `DELETE /tasks/<task_id>`: Deletes a task by its ID.

**Pagination:**

The `/tasks` endpoint supports pagination. You can specify the `page` and `per_page` query parameters to retrieve a specific page of tasks. By default, `page` is set to 0 and `per_page` is set to 10.

**Error Handling:**

The API handles common errors and provides appropriate error responses. For example, if you try to retrieve a task that does not exist, you will receive a 404 Not Found response.

**Conclusion:**

This Task Management RESTful API provides basic CRUD operations for managing tasks. It can be used as a starting point for building more advanced task management systems or integrated into existing applications.



