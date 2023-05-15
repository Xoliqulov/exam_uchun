import logging
import re
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = os.getenv('TOKEN', 'default_token_value')

logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_handler(msg: types.Message):
    await msg.answer(f"Hush kelibsiz {msg.from_user.first_name} 👋 \nBu bot gruppada kelgan oxirgi xabarni ochiradi")


@dp.message_handler()
async def handle_messages(message: types.Message):
    if len(re.findall(r'[aeiouAEIOU]', message.text)) > 5:
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
