'''
beanie docs - https://beanie-odm.dev/tutorial/finding-documents/
'''
from fastapi import APIRouter, HTTPException
from models import Task
from typing import List

'''
PydanticObjectId - это подкласс Pydantic, предоставляемый в 
библиотеке Beanie. Он используется для работы с идентификаторами 
объектов MongoDB типа ObjectId.
'''
from beanie import PydanticObjectId


task_router = APIRouter()

#маршрут получения всех задач
@task_router.get('/')
async def get_all_tasks() -> List[Task]:
    # .find_all() - метод биня
    tasks = await Task.find_all().to_list()
    return tasks

# маршрут добавления задачи
@task_router.post('/')
async def create_tasks(task:Task):
    await task.create()
    return {"message":"task added"}

# маршрут получения задачи по id
@task_router.get('/{task_id}')
async def retrive_task_by_id(task_id:PydanticObjectId) -> Task:
    task_to_get = await Task.get(task_id)
    return task_to_get


@task_router.put('/{task_id}')
async def update_task(task:Task,task_id:PydanticObjectId) -> Task:
    task_to_update = await Task.get(task_id)
    
    if not task_to_update:
        raise HTTPException(
            status_code=404,
            detail = f"task with {task_id} is not found"
        )
        
    task_to_update.task_content = task.task_content
    task_to_update.is_completed = task.is_completed
    await task_to_update.save()
    
    return task_to_update
   

@task_router.delete('/{task_id}')
async def delete_task_by_id(task_id:PydanticObjectId):
    task_to_delete = await Task.get(task_id)
    await task_to_delete.delete()
    return {"message":"Task deleted successfully"}