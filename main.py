import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from src.bot.init_bot import bot, dp
from src.database.crud import save_or_update_user_to_db
from src.bot.keyboards import get_start_panel, get_card_panel
from src.utils.parser_auto_parts import parse_random_part


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    # (id=392539649, is_bot=False, first_name='Владислав', last_name='Бабенко', username='vlad_bb', language_code='en',
    user_data = {"user_id": message.from_user.id, "first_name": message.from_user.first_name,
                 "last_name": message.from_user.last_name, "username": message.from_user.username,
                 "language_code": message.from_user.language_code}
    await save_or_update_user_to_db(user_data)
    panel = await get_start_panel()
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}!",
                         reply_markup=panel)


@dp.message(Command("parse"))
async def command_parse_handler(message: Message) -> None:
    """
    This handler receives messages with `/parse` command
    """
    part_data = await parse_random_part()
    panel = await get_card_panel(url=part_data.get("item_card"))
    caption = f"{part_data.get('item_name')}\n{part_data.get('item_price')}"
    await bot.send_photo(chat_id=message.from_user.id, photo=part_data.get("image_link"), caption=caption,
                         reply_markup=panel)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())  # запуск Бота
    # print(asyncio.run(parse_random_part()))  # для тестування
