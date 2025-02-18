import json

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Task 1',
        'is_deleted': False,
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Task 2',
        'is_deleted': False,
    }
]

"""
Create 
Read - Get all, Get by ID
Update
Delete
"""


@app.get("/")
def ping():
    return {"message": "Server is up and running!"}


@app.get("/tasks", summary="Get all tasks", tags=["tasks"])
def get_all_tasks():
    return Response(json.dumps(tasks), status_code=200, media_type='application/json')


# url: localhost:8080/get_tasks_by_id/1
@app.get("/tasks/{task_id}", summary="Get task by ID", tags=["tasks"])
def get_task_by_id(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return Response(json.dumps(task), status_code=200, media_type='application/json')
    return Response(json.dumps({'error': 'task not found'}), status_code=404, media_type='application/json')


class Task(BaseModel):
    title: str
    description: str


@app.post("/tasks", summary="Create new task", tags=["tasks"])
def create_task(task: Task):
    task_dict = task.dict()
    task_dict['id'] = len(tasks) + 1
    task_dict['is_deleted'] = False

    tasks.append(task_dict)

    return Response(json.dumps({'message': 'successfully added new task'}), status_code=201,
                    media_type='application/json')


@app.put("/tasks/{task_id}", summary="Update task by ID", tags=["tasks"])
def update_task(task_id: int, task: Task):
    for task_dict in tasks:
        if task_dict['id'] == task_id:
            task_dict['title'] = task.title
            task_dict['description'] = task.description
            return Response(
                json.dumps({'message': 'successfully updated task'}),
                status_code=200,
                media_type='application/json')

    return Response(json.dumps({'error': 'task with this ID not found'}), status_code=404,
                    media_type='application/json')


@app.delete("/tasks/{task_id}", summary="Delete task by ID", tags=["tasks"])
def delete_task(task_id: int):
    for task_dict in tasks:
        if task_dict['id'] == task_id:
            tasks.pop(tasks.index(task_dict))
            return Response(json.dumps({'message': 'successfully deleted task'}),
                            status_code=200,
                            media_type='application/json')

    return Response(json.dumps({'error': 'task with this ID not found'}), status_code=404,
                    media_type='application/json')
