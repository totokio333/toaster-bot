from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio
import random

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

moods = ["в восторге", "раздражён", "спокойный", "в панике", "сонный"]

async def change_mood():
    while True:
        await asyncio.sleep(60)
        mood = random.choice(moods)
        logging.info(f"Настроение тостера: {mood}")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я Тостер-бот. Готов к поджарке!")

@dp.message_handler(commands=['mood'])
async def current_mood(message: types.Message):
    mood = random.choice(moods)
    await message.reply(f"Тостер сейчас {mood}.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(change_mood())
    executor.start_polling(dp, skip_updates=True)
