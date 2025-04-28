from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from handlers import start, register, matchmaking, profile, invite, check_invites
import logging
import asyncio

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

start.register_handlers_start(dp)
register.register_handlers_register(dp)
matchmaking.register_handlers_matchmaking(dp)
profile.register_handlers_profile(dp)
invite.register_handlers_invite(dp)
check_invites.register_handlers_check_invites(dp)

async def on_startup(_):
    print("Bot is online.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
