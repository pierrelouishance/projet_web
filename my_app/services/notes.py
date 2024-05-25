from datetime import datetime

from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload

#from my_app.schemas import TaskSchema, NewTaskSchema, CommentSchema
from my_app.database import Session
# from my_app.models.task import Task



# by PL
def get_all_tasks() -> list[TaskSchema]:
    with Session() as session:
        statement = select(Task).options(joinedload(Task.comments))
        tasks_data = session.scalars(statement).unique().all()
        return [
            TaskSchema(
                id=task.id,
                name=task.name,
                description=task.description,
                creation_date=task.creation_date,
                comments=[
                    CommentSchema(id=comment.id, message=comment.message)
                    for comment in task.comments
                ]
            )
            for task in tasks_data
        ]
    
