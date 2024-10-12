from aiogram import Router, F
from aiogram.filters.command import Command
from . import start
from . import help
from . import replay
from . import inline
from . import get
from . import echo

user_router = Router()

user_router.message.register(start.welcome, F.text=="/start")
user_router.message.register(help.help, F.text=="/help")
user_router.message.register(replay.replay_answer, F.text=="/replay")
user_router.message.register(inline.home, F.text=="/inline")
user_router.message.register(get.get_answer)

user_router.message.register(echo.echo)