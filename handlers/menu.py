from aiogram import Router, types
from aiogram.filters import Command
from keyboards.main_menu import main_menu_keyboard
from keyboards.inline_menu import fake_disconnect_keyboard
from database import get_user
import random
import asyncio

router = Router()

@router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("منوی اصلی:", reply_markup=main_menu_keyboard())

@router.message(lambda message: message.text == "شروع چت جدید ✨")
async def start_chat(message: types.Message):
    user = get_user(message.from_user.id)
    if not user:
        await message.answer("شما ابتدا باید ثبت نام کنید! /start")
        return

    fake_usernames = ["Ali_Star", "NiloofarQueen", "Amir_Hero", "SaraSmile"]
    fake_username = random.choice(fake_usernames)

    await message.answer(f"شما به {fake_username} متصل شدید! لطفا پیام خود را ارسال کنید.")

    disconnect_chance = random.randint(1, 100)
    if disconnect_chance <= 15:
        await asyncio.sleep(15)
        await message.answer(f"چت توسط {fake_username} قطع شد.", reply_markup=fake_disconnect_keyboard())

    await asyncio.sleep(random.randint(600, 1200))  # 10 تا 20 دقیقه
    await message.answer(f"چت به طور خودکار توسط {fake_username} قطع شد.", reply_markup=fake_disconnect_keyboard())

@router.message(lambda message: message.text == "مشاهده پروفایل من 📄")
async def view_profile(message: types.Message):
    user = get_user(message.from_user.id)
    if not user:
        await message.answer("شما ابتدا باید ثبت نام کنید! /start")
        return
    await message.answer(
        f"نام: {user['name']}\n"
        f"جنسیت: {user['gender']}\n"
        f"سن: {user['age']}\n"
        f"تاریخ ثبت‌نام: {user['created_at']}"
    )

@router.message(lambda message: message.text == "تنظیمات ⚙️")
async def settings(message: types.Message):
    await message.answer("بخش تنظیمات در دست ساخت است...")
