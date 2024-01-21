import motor, motor.motor_asyncio, beanie
from models import Task

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    
    await beanie.init_beanie(
        database=client.db_name,
        document_models=[Task]
    )
        

