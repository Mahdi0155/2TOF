from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboards.main_menu import main_menu_keyboard
from states import RegisterStates
from database import add_user, get_user
from datetime import datetime

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id)
    if user:
        await message.answer("شما قبلا ثبت نام کردید!", reply_markup=main_menu_keyboard())
    else:
        await message.answer("سلام! لطفا نام خود را وارد کنید:")
        await state.set_state(RegisterStates.waiting_for_name)

@router.message(RegisterStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("جنسیت خود را وارد کنید (مرد/زن):")
    await state.set_state(RegisterStates.waiting_for_gender)

@router.message(RegisterStates.waiting_for_gender)
async def process_gender(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['مرد', 'زن']:
        await message.answer("لطفا مرد یا زن وارد کنید.")
        return
    await state.update_data(gender=message.text.lower())
    await message.answer("سن خود را وارد کنید:")
    await state.set_state(RegisterStates.waiting_for_age)

@router.message(RegisterStates.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("سن باید عدد باشد.")
        return
    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        name=data['name'],
        gender=data['gender'],
        age=int(message.text)
    )
    await message.answer("ثبت نام شما با موفقیت انجام شد!", reply_markup=main_menu_keyboard())
    await state.clear()
