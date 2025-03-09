import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from environs import env

from app.user import user
from app.cmd import cmd
from app.database.models import async_main

env.read_env()


async def main():    
    bot = Bot(token=env.str('TOKEN'),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp = Dispatcher()
    dp.include_routers(cmd, user)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    commands = [
        BotCommand(command='start', description='Start bot'), 
        BotCommand(command='help', description='Help you'), 
        BotCommand(command='getinfo', description='get user info')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await async_main()
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
