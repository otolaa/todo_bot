from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.database.requests import set_user, dell_task, set_task, get_mess
import app.keyboards as kb

user = Router()

suffix = '~'
separator = suffix * 30


@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(tid=message.from_user.id, username=message.from_user.username)
    mess = await get_mess()
    await message.answer(text = '\n'.join(mess),
                         reply_markup = await kb.tasks(tid=message.from_user.id))

@user.callback_query(F.data.startswith('task_'))
async def delete_task(callback: CallbackQuery):
    await dell_task(int(callback.data.split('_')[1]))
    mess = await get_mess()
    mess.insert(0, 'Успешно удалена')
    mess.insert(1, separator)
    await callback.message.edit_text(text = '\n'.join(mess),
                                  reply_markup = await kb.tasks(tid=callback.from_user.id))

@user.message()
async def add_task(message: Message):
    if len(message.text) > 150:
        await message.answer('Текст задания должен быть <= 150 символов')
        return

    await set_task(message.from_user.id, message.text)
    mess = await get_mess()
    mess.insert(0, 'Успешно добавлена')
    mess.insert(1, separator)
    await message.answer(text = '\n'.join(mess),
                         reply_markup = await kb.tasks(tid=message.from_user.id))
