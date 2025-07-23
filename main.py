import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

API_TOKEN = os.getenv("BOT_TOKEN", "8085303818:AAE1G-ekS5pWFqdTIR0eibXCMoWYNs77RaU")
CHANNEL_USERNAME = "@your_channel_4"

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

async def check_subscription(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ("member", "administrator", "creator")
    except Exception:
        return False

@dp.message(CommandStart())
async def start_handler(message: Message, bot: Bot):
    user_id = message.from_user.id
    is_subscribed = await check_subscription(bot, user_id)
    if is_subscribed:
        await message.answer("✅ Вы подписаны на канал!")
    else:
        await message.answer(
            f"❌ Вы не подписаны на канал {CHANNEL_USERNAME}.\n"
            f"Пожалуйста, подпишитесь и нажмите /start снова."
        )

async def main():
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
