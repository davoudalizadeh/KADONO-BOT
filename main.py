import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# خواندن توکن از تنظیمات محیطی سرور
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.reply(
        "سلام! من دستیار یادآوری رویداد و پیشنهاد هدیه هستم 🎁\n"
        "به زودی بهت کمک می‌کنم هیچ تولد و سالگردی رو فراموش نکنی!"
    )

async def main():
    print("ربات با موفقیت روشن شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
