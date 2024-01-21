from fastapi import FastAPI
from task import task_router
from database import init_db

app = FastAPI(
    title="Task app",
    description="This is a simple api for tasks"
)

app.include_router(task_router, prefix='/tasks')

@app.on_event("startup")
async def db_start():
    await init_db()