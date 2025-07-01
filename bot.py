import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

async def send_heartbeat():
    await bot.send_message(CHAT_ID, f"✅ Бот работает. Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Бот запущен и отслеживает листинги.")

async def on_startup(_):
    scheduler.add_job(send_heartbeat, "interval", hours=5)
    scheduler.start()
    await send_heartbeat()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)