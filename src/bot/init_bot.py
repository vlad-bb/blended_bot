import os
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.enums import ParseMode


config = dotenv_values(".env")

# Bot token can be obtained via https://t.me/BotFather

TOKEN = config.get("BOT_TOKEN") if config.get("BOT_TOKEN") else os.environ.get("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)
