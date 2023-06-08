# Grey_dot_backend

This project is a simple RESTful API for managing tasks. It allows you to create, retrieve, update, and delete tasks. The tasks are stored in a SQLite database, and the API is implemented using Python and Flask.

Features:

Create a new task: You can create a new task by providing the task details such as title, description, due date, and status.
Retrieve a single task: You can retrieve a task by its ID.
Update an existing task: You can update the details of an existing task.
Delete a task: You can delete a task by its ID.
List all tasks: You can retrieve a paginated list of all tasks.
API Endpoints:

GET /tasks: Retrieve a paginated list of all tasks.
GET /tasks/<task_id>: Retrieve a single task by its ID.
POST /tasks: Create a new task.
PUT /tasks/<task_id>: Update an existing task.
DELETE /tasks/<task_id>: Delete a task by its ID.
Getting Started:

To set up and run the project locally, follow these steps:

Clone the repository: git clone <repository_url>
Create a virtual environment: python3 -m venv env
Activate the virtual environment:
For Windows: .\env\Scripts\activate
For Linux/Mac: source env/bin/activate
Install the dependencies: pip install -r requirements.txt
Create a SQLite database file named tasks.db.
Run the application: python app.py
The API will be accessible at http://localhost:5000.

Usage:

Once the API is up and running, you can make HTTP requests to interact with the endpoints. Here are some example requests using cURL:

Create a new task:

vbnet
Copy code
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "Task 1",
  "description": "Complete task 1",
  "due_date": "2023-06-8",
  "status": "Incomplete"
}' http://localhost:5000/tasks
Retrieve a single task:

bash
Copy code
curl http://localhost:5000/tasks/<task_id>
Update an existing task:

vbnet
Copy code
curl -X PUT -H "Content-Type: application/json" -d '{
  "title": "Updated Task",
  "status": "In Progress"
}' http://localhost:5000/tasks/<task_id>
Delete a task:

bash
Copy code
curl -X DELETE http://localhost:5000/tasks/<task_id>
List all tasks:

bash
Copy code
curl http://localhost:5000/tasks?page=<page_number>&per_page=<tasks_per_page>
Pagination:

The /tasks endpoint supports pagination. You can specify the page and per_page query parameters to retrieve a specific page of tasks. By default, page is set to 1 and per_page is set to 10.

Error Handling:

The API handles common errors and provides appropriate error responses. For example, if you try to retrieve a task that does not exist, you will receive a 404 Not Found response.

Conclusion:

This Task Management RESTful API provides basic CRUD operations for managing tasks. It can be used as a starting point for building more advanced task management systems or integrated into existing applications.

Please refer to the API documentation or the source code for further details on the available endpoints and data structures
