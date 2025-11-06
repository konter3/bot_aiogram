from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

with open(r"..\.venv\env") as file:
	Bot_token = file.readline()

bot = Bot(token=Bot_token)
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def proc_command_start (message: Message):
	await message.answer("Привет! Это эхо бот")

@dp.message(Command(commands="help"))
async def proc_command_help (message: Message):
	await message.answer("Этот бот возвращает то, что ты ему пишешь")

@dp.message()
async def echo_send (message: Message):
	await message.reply(text=message.text)

if __name__ == '__main__':
	dp.run_polling(bot)
