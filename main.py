from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/soup', description='Команда для того, чтобы узнать, какие есть сапы'),
        types.BotCommand(command='/salad', description='Команда для того, чтобы узнать, какие есть салаты'),
        types.BotCommand(command='/dish', description='Команда для того, чтобы узнать, список блюд в наличии')
    ]

    await  bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой эхо бот')

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с ......')

@dp.message_handler(commands= 'soup')
async def start(message: types.Message):
    await message.answer('Я могу предложить эти супы')

@dp.message_handler(commands= 'salad')
async def start(message: types.Message):
    await message.reply('Я могу предложить эти салаты')

@dp.message_handler(commands= 'dish')
async def start(message: types.Message):
    await message.reply('Я могу предложить этот список блюд')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await  set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)
