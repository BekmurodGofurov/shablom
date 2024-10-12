from aiogram.types import Message

async def help(message: Message):
    await message.answer(f"/start - botni qayta ishga tushirish\n/help - yordam olish")