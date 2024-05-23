import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from convert import convert

dp = Dispatcher()


@dp.message()
async def message_handler(message: Message):
    try:
        response = convert(message.text)
    except:
        response = "Иди нахуй"
    await message.reply(response)


async def main():
    token = os.environ["BOT_TOKEN"]
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
