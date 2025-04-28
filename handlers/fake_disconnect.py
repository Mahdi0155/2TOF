from aiogram import Router, types
from keyboards.inline_menu import fake_disconnect_keyboard
from database import get_user
import random

router = Router()

@router.callback_query(lambda c: c.data == "fake_disconnect")
async def fake_disconnect(call: types.CallbackQuery):
    user = get_user(call.from_user.id)
    if not user:
        await call.message.answer("شما ابتدا باید ثبت نام کنید! /start")
        return

    await call.message.edit_text("چت توسط شما قطع شد.", reply_markup=None)
