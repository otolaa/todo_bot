from app.database.models import async_session
from app.database.models import User, Task
from sqlalchemy import select, update, delete, desc


async def get_mess():
    return [
        'Нажмите на задачу чтобы удалить,',
        'или напишите новую.',
    ]

async def set_user(tid: int, username: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == tid))
        
        if not user:
            session.add(User(id=tid, username=username))
            await session.commit()

async def get_tasks(tid: int):
    async with async_session() as session:
        return await session.scalars(select(Task).where(Task.user == tid).order_by(desc(Task.id)))

async def set_task(tid: int, title: str):
    async with async_session() as session:
        session.add(Task(title = title, user = tid))
        await session.commit()

async def dell_task(task_id: int):
    async with async_session() as session:
        await session.execute(delete(Task).where(Task.id == task_id))
        await session.commit()