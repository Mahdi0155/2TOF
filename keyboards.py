from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("💬 شروع چت جدید"),
    KeyboardButton("🧑‍💻 پروفایل"),
    KeyboardButton("⭐ عضویت ویژه"),
)
main_menu.add(
    KeyboardButton("➕ دعوت دوستان"),
    KeyboardButton("ℹ️ قوانین")
)

def end_chat_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("❌ پایان چت", callback_data="end_chat"))
    return kb

def accept_decline_kb():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("✅ قبول", callback_data="accept_chat"),
        InlineKeyboardButton("❌ رد", callback_data="decline_chat")
    )
    return kb
