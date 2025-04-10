from aiogram import types
from aiogram.dispatcher import FSMContext
from database import *

async def register_handlers(dp):
    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):
        await message.answer("👋 Добро пожаловать в анонимный чат!\n"
                           "Используй /find чтобы начать поиск")

    @dp.message_handler(commands=['find'])
    async def cmd_find(message: types.Message):
        user = await get_user(message.from_user.id)
        if not user:
            await message.answer("Сначала заполни анкету!")
            return
        
        partner = await find_partner(message.from_user.id)
        if partner:
            await message.answer(f"🔞 Найден партнер: {partner['username']}")
        else:
            await message.answer("😔 Пока нет подходящих партнеров")

    @dp.message_handler(commands=['profile'])
    async def cmd_profile(message: types.Message):
        user = await get_user(message.from_user.id)
        await message.answer(
            f"📊 Твой профиль:\n"
            f"Уровень: {user['level']}\n"
            f"Сердец: {user['hearts']}"
        )
