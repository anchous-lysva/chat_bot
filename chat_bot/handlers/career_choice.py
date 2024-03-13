from aiogram import types, F, Router # F - filter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext # fsm машина состояний
from aiogram.fsm.state import StatesGroup, State # состояние state
from keyboards.prof_keyboards import make_row_keyboard

router = Router() # маршрутизация

available_prof_names = ['Разработчик', 'Аналитик', 'Тестировщик']
available_prof_grades = ['Junior', 'Middle', 'Senior']

class ChoiceProfNames(StatesGroup): # группа состояний
    choice_prof_names = State() # первый шаг
    choice_prof_grades = State() # второй шаг

#Хэндлер на команду /prof
@router.message(Command('prof')) # оборачиваем функцию в декоратор
async def cmd_prof(message: types.Message, state: FSMContext): # хендлер
    name = message.chat.first_name 
    await message.answer(f'Привет, {name}, выбери свою профессию', 
        reply_markup=make_row_keyboard(available_prof_names))
    
    await state.set_state(ChoiceProfNames.choice_prof_names) # устанавливаем "галочку" о том, что зафиксировали состояние
    # после этого хэндлера мы будем находиться на этом состоянии

@router.message(ChoiceProfNames.choice_prof_names, F.text.in_(available_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext): # хендлер
    await state.update_data(chosen_prof=message.text.lower()) # сохранили ответ пользователя в виде ключ=значение
    await message.answer(text='Спасибо, теперь выбери свой уровень', 
        reply_markup=make_row_keyboard(available_prof_grades))
    await state.set_state(ChoiceProfNames.choice_prof_grades) # поменяли состояние на следующее

@router.message(ChoiceProfNames.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(f'Я не знаю такой профессии', 
        reply_markup=make_row_keyboard(available_prof_names))


@router.message(ChoiceProfNames.choice_prof_grades, F.text.in_(available_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext): # хендлер
    user_data = await state.get_data() # записываем полученные данные как словарь
    await message.answer(f'Вы выбрали {message.text.lower()} уровень. Ваша профессия {user_data.get("chosen_prof")}', 
        reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(ChoiceProfNames.choice_prof_grades)
async def grade_chosen_incorrectly(message: types.Message):
    await message.answer(f'Я не знаю такого уровня', 
        reply_markup=make_row_keyboard(available_prof_grades))