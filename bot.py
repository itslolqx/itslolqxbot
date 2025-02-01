import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "7558726763:AAHjgT38QegjAcMup2xsrclm2AfZ46hQLxI"
GEMINI_API_KEY = "AIzaSyAcFq5gJ5B4qZaRM7aK96-4-sNUMxQ-N0M"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@dp.message_handler()
async def handle_message(message: types.Message):
    response = model.generate_content(message.text)
    await message.reply(response.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)