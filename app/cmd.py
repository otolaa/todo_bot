from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime, timedelta, timezone

cmd = Router()

version_relise = '0.0.1'
suffix = '~'
separator = suffix * 30
tz_msk = timezone(timedelta(hours=3)) 


@cmd.message(F.text, Command("help"))
async def cmd_help(message: Message):    
    mess = [
        f'Sample ToDo Bot',
        separator,
        f'This bot is working with the:',
        f'aiogram 3.x and SQLAlchemy 2.x',
        separator,
        f'https://github.com/otolaa/todo_bot'
    ]

    await message.answer(text = '\n'.join(mess), disable_web_page_preview = True)

@cmd.message(F.text, Command("getinfo"))
async def cmd_getinfo(message: Message):
    name = f'{message.from_user.first_name}'
    if message.from_user.last_name is not None: 
        name = f'{message.from_user.first_name} {message.from_user.last_name}'
    
    mess = [
        f'@{message.from_user.username}',
        f'{name}',
        separator,
        f'cid: {message.chat.id}',
        f'mid: {message.message_id}',
        f'uid: {message.from_user.id}',        
        separator,
        f'{datetime.now(tz_msk).strftime("%d.%m.%y %H:%M %z")}',
        f'ver: {version_relise}'
    ]

    await message.answer(text = '\n'.join(mess), disable_web_page_preview = True)
