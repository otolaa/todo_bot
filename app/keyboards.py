from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_tasks


async def tasks(tid):
    tasks = await get_tasks(tid)
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text=f'✓{task.id} ~ {task.title}', 
                                          callback_data = f'task_{task.id}'))
    
    return keyboard.adjust(1).as_markup()