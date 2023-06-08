from flask import request
from services import create_task, get_task, update_task, delete_task, get_all_tasks,fetch_tasks_from_database
from models import Task

def create_task_data(task_data):
    # Parse task data from request and create a new task
    title = task_data.get('title')
    description = task_data.get('description')
    due_date = task_data.get('due_date')
    status = task_data.get('status')

    new_task = Task(None, title, description, due_date, status)

    # Save the task and return the created task object
    created_task = create_task(new_task)
    return created_task

def get_task_data(task_id):
    # Get a task by its ID
    task = get_task(task_id)
    return task

def update_task_data(task_id, task_data):
    # Update an existing task
    title = task_data.get('title')
    description = task_data.get('description')
    due_date = task_data.get('due_date')
    status = task_data.get('status')

    updated_task = update_task(task_id, title, description, due_date, status)
    return updated_task

def delete_task_data(task_id):
    # Delete a task
    result = delete_task(task_id)
    return result

def get_all_tasks_data():
    # Get all tasks
    tasks = get_all_tasks()
    return tasks

def fetch_tasks_data_from_database(offset,limit):
    #Get tasks based on pagination
    tasks=fetch_tasks_from_database(offset,limit)
    return tasks
