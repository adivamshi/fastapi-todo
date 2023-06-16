import uuid
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
from logging.handlers import TimedRotatingFileHandler

app = FastAPI()

# Set up logging configuration
log_file = "server.log"
log_handler = TimedRotatingFileHandler(log_file, when="midnight", backupCount=5)
log_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Middleware to log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request received: {request.method} {request.url}")
    response = await call_next(request)
    return response


class Task(BaseModel):
    id: str = ""
    desc: str
    done: bool = False


class Todo:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task: Task):
        task.id = str(uuid.uuid4())
        self.tasks[task.id] = task
        return {"task_id": task.id}

    def read_task(self, task_id: str):
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, updated_task: Task):
        if task_id in self.tasks:
            updated_task.id = task_id
            self.tasks[task_id] = updated_task
            return updated_task
        return None

    def delete_task(self, task_id: str):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return {"message": "Task deleted"}
        return None

    def mark_task_as_done(self, task_id: str):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.done = True
            return task
        return None


todo = Todo()


@app.post("/tasks/")
def create_task(task: Task):
    return todo.create_task(task)


@app.get("/tasks/{task_id}")
def read_task(task_id: str):
    task = todo.read_task(task_id)
    if task:
        return task
    else:
        return {"message": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    task = todo.update_task(task_id, updated_task)
    if task:
        return task
    else:
        return {"message": "Task not found"}


@app.put("/tasks/{task_id}/done")
def mark_task_as_done(task_id: str):
    task = todo.mark_task_as_done(task_id)
    if task:
        return task
    else:
        return {"message": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    result = todo.delete_task(task_id)
    if result:
        return result
    else:
        return {"message": "Task not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
