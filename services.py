import sqlite3
from models import Task
import threading
import json

# Create a thread-local storage for SQLite connections
thread_local = threading.local()
def get_connection():
    # Check if a connection already exists for the current thread
    if hasattr(thread_local, 'connection'):
        return thread_local.connection

    # Create a new connection for the current thread
    connection = sqlite3.connect('tasks.db')

    # Store the connection in the thread-local storage
    thread_local.connection = connection

    return connection

def initialize_database():
    # Create the tasks table if it doesn't exist
    connection = get_connection()
    c = connection.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  due_date TEXT,
                  status TEXT NOT NULL)''')

    connection.commit()
    c.close()

def create_task(task):
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()

    # Insert a new task into the database
    c.execute('''INSERT INTO tasks (title, description, due_date, status)
                 VALUES (?, ?, ?, ?)''',
              (task.title, task.description, task.due_date, task.status))
    connection.commit()

    # Get the ID of the created task
    task_id = c.lastrowid

    # Retrieve the created task from the database
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    result = c.fetchone()

    # Create a Task object from the retrieved data
    created_task = Task(result[0], result[1], result[2], result[3], result[4])

    # Close the cursor
    c.close()

    return created_task

def get_task(task_id):
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()

    # Retrieve a task from the database by its ID
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    result = c.fetchone()

    if result:
        # Create a Task object from the retrieved data
        task = Task(result[0], result[1], result[2], result[3], result[4])
        return task
    else:
        return None

def update_task(task_id, title, description, due_date, status):
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()

    # Update an existing task in the database
    c.execute('''UPDATE tasks
                 SET title = ?, description = ?, due_date = ?, status = ?
                 WHERE id = ?''',
              (title, description, due_date, status, task_id))
    connection.commit()

    # Retrieve the updated task from the database
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    result = c.fetchone()

    if result:
        # Create a Task object from the retrieved data
        updated_task = Task(result[0], result[1], result[2], result[3], result[4])
        return updated_task
    else:
        return None

def delete_task(task_id):
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()
    # Check if the ID is present 
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    res=c.fetchall()
    if res:
        # Delete a task from the database by its ID
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        connection.commit()
        # Close the cursor
        c.close()
        print(res)
        return 1
    else:
        # If ID is not present
        return 0

def get_all_tasks():
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()

    # Retrieve all tasks from the database
    c.execute('SELECT * FROM tasks')
    results = c.fetchall()

    tasks = []

    # Create Task objects from the retrieved data
    for result in results:
        task = Task(result[0], result[1], result[2], result[3], result[4])
        tasks.append(task)

    # Close the cursor
    c.close()

    return tasks
def fetch_tasks_from_database(offset, limit):
    # Retrieve the connection for the current thread
    connection = get_connection()

    # Create a cursor using the connection
    c = connection.cursor()

    # Retrieve tasks from the database with pagination
    c.execute('SELECT * FROM tasks LIMIT ? OFFSET ?', (limit, offset))
    results = c.fetchall()

    tasks = []

    # Create Task objects from the retrieved data
    for result in results:
        task = Task(result[0], result[1], result[2], result[3], result[4])
        tasks.append(task)

    # Close the cursor
    c.close()

    return tasks

# Initialize the database
initialize_database()
