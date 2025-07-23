import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

API_TOKEN = os.getenv("BOT_TOKEN", "8085303818:AAE1G-ekS5pWFqdTIR0eibXCMoWYNs77RaU")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я простой Telegram-бот.")

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
