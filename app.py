from flask import Flask, jsonify, request
from controllers import create_task_data, get_task_data, update_task_data, delete_task_data, get_all_tasks_data,fetch_tasks_data_from_database
from models import Task
import json
app = Flask(__name__)

def task_encoder(obj):
    if isinstance(obj, Task):
        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "due_date": obj.due_date,
            "status": obj.status
        }
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

# Create a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    new_task = create_task_data(task)
    json_tasks = json.dumps(new_task, default=task_encoder)
    return json_tasks, 201

# Retrieve a single task by its ID
@app.route('/tasks/<task_id>', methods=['GET'])
def get_single_task(task_id):
    task = get_task_data(task_id)
   
    if task:
        json_tasks = json.dumps(task, default=task_encoder)
        return json_tasks, 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# Update an existing task
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_single_task(task_id):
    task_data = request.get_json()
    updated_task = update_task_data(task_id, task_data)
    if updated_task:
        json_tasks = json.dumps(updated_task, default=task_encoder)
        return json_tasks, 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# Delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_single_task(task_id):
    result = delete_task_data(task_id)
    if result==1:
        return jsonify({'message': 'Task deleted'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# List all tasks
@app.route('/tasks', methods=['GET'])

def get_tasks():
    # Get query parameters for pagination
    page = int(request.args.get('page', 0))
    per_page = int(request.args.get('per_page', 10))
    if page==0:
         tasks = get_all_tasks_data()
         json_tasks = json.dumps(tasks, default=task_encoder)
         return json_tasks, 200
    # Calculate the offset based on the page and per_page values
    offset = (page - 1) * per_page

    # Retrieve tasks from the database with pagination
    tasks = fetch_tasks_data_from_database(offset, per_page)

    # Serialize tasks to JSON using the custom encoder
    json_tasks = json.dumps(tasks, default=task_encoder)

    return json_tasks,210


   

if __name__ == '__main__':
    app.run()
