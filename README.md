# FastAPI Server
This is a FastAPI server that provides CRUD operations for managing tasks. It exposes a RESTful API for creating, reading, updating, and deleting tasks. The server is implemented in Python using FastAPI framework.

## Requirements
* Python 3.7 or above
* FastAPI
* Uvicorn
* Pydantic
## Installation
1. Clone the repository:
```bash
git clone <repository_url>
cd fastapi-server
```
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```
2. The server should now be running at http://localhost:8000. You can access the API endpoints using a tool like cURL or a REST client like Postman.
## API Endpoints
The following endpoints are available:

* `POST /tasks/`: Create a new task.
* `GET /tasks/{task_id}`: Retrieve a task by ID.
* `PUT /tasks/{task_id}`: Update a task by ID.
* `PUT /tasks/{task_id}/done`: Mark a task as done by ID.
* `DELETE /tasks/{task_id}`: Delete a task by ID.
## Request/Response Examples
### Create a Task
Request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"desc": "Task 1"}' http://localhost:8000/tasks/
```
Response:

```json
{
  "task_id": "1a2b3c4d"
}
```
### Retrieve a Task
Request:

```bash
curl -X GET http://localhost:8000/tasks/1a2b3c4d
```
Response:

```json
{
  "id": "1a2b3c4d",
  "desc": "Task 1",
  "done": false
}
```
### Update a Task
Request:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"desc": "Updated Task"}' http://localhost:8000/tasks/1a2b3c4d
```
Response:

```json
{
  "id": "1a2b3c4d",
  "desc": "Updated Task",
  "done": false
}
```
### Mark a Task as Done
Request:

```bash
curl -X PUT http://localhost:8000/tasks/1a2b3c4d/done
```
Response:

```json
{
  "id": "1a2b3c4d",
  "desc": "Updated Task",
  "done": true
}
```
### Delete a Task
Request:

```bash
curl -X DELETE http://localhost:8000/tasks/1a2b3c4d
```
Response:

```json
{
  "message": "Task deleted"
}
```
## Logging
The server logs every request received. The logs are saved to a rolling log file server.log with rotation performed every day.

## Error Handling
The server includes custom exception handlers to handle HTTP exceptions and other general exceptions. Detailed error messages are returned as JSON responses with appropriate status codes.
