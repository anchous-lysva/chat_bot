from aiogram import types, F, Router # F - filter
from aiogram.filters.command import Command
import logging
# import random
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox

router = Router() # маршрутизация

#Хэндлер на команду /start
@router.message(Command('start')) # оборачиваем функцию в декоратор
async def cmd_start(message: types.Message): # хендлер
    name = message.chat.first_name 
    await message.answer(f'Привет, {name}', reply_markup=kb1)

#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

# Хэндлер на команду /info
@router.message(F.text == 'Информация')
@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я бот - твой друг и товарищ ")

#Хэндлер на команду /fox (навешиваем столько декораторов, сколько нужно)
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}') # отвечаем текстом и картинкой пользователю, который ввел одну из команд
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox) # рассылает фото всем, с кем уже начат диалог (рассылка по id)

#Хендлер на сообщения (любой ввод, который не отработался в предыдущих командах)
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji='😎')
    elif 'лиса' in msg_user:
        await message.answer(f'Я бот, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')