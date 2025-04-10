from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрация команд
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand("start", "Начать работу"),
        types.BotCommand("find", "Найти собеседника"),
        types.BotCommand("profile", "Мой профиль")
    ]
    await bot.set_my_commands(commands)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
