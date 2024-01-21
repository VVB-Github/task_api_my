# О Document - https://beanie-odm.dev/api-documentation/document/#documentcreate
from beanie import Document
from pydantic import Field
from datetime import datetime

class Task(Document):
    task_content:str = Field(max_length=400)
    is_completed: bool
    date_created: datetime = datetime.now()
    
    class Settings:
        '''
        Когда вы определяете класс модели в Beanie (асинхронном 
        Object-Document Mapper для MongoDB), вы можете использовать 
        класс Settings для настройки различных параметров, таких как 
        имя коллекции. В данном случае, name = "task_database" указывает,
        что документы, созданные с использованием модели Task, будут 
        храниться в коллекции с именем "task_database".
        '''
        name = "task_database2"
        
    class Config:
        json_schema_extra = {
            "task_content":"content basic",
            "is_completed": False,
            "date_created": datetime.now()
        }