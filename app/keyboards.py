from datetime import datetime, timedelta, timezone
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_tasks


async def tasks(tid):
    tasks = await get_tasks(tid)
    tz_msk = timezone(timedelta(hours=3))
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        t = datetime.fromtimestamp(task.created_at).astimezone(tz_msk).strftime("%d.%m %H:%M")
        keyboard.add(InlineKeyboardButton(text=f'✓{task.id} ~ {task.title} ~ {t}', 
                                          callback_data = f'task_{task.id}'))
    
    return keyboard.adjust(1).as_markup()