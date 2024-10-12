from aiogram.types import BotCommand

async def set_bot_commands(bot):
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni qayta ishga turshirish!"),
        BotCommand(command="/link", description="Get user profile user"),
        BotCommand(command="/inline", description="Inline tugama!"),
        BotCommand(command="/replay", description="Reply tugma!"),
        BotCommand(command="/help", description="Yordam olish!")

    ])