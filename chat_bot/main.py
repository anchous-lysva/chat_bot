import asyncio
import config
from aiogram import Bot, Dispatcher, types, F # F - filter
import logging
from handlers import common, career_choice


async def main(): # зацикливаем бот стартовать асинхронной функцией
    #Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    #Создаем главный объект бота
    bot = Bot(token=config.token)

    #Создаем диспечера
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)
    

    await dp.start_polling(bot)

if __name__ == "__main__": # запуск функции только из файла main.py
    asyncio.run(main())