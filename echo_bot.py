from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

#inithelithetion the bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#start the bot
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi, my name is Damir")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("write something to me")

#turn on the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

