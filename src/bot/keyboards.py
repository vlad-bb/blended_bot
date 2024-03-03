from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


async def get_start_panel():
    buttons = [[KeyboardButton(text="/parse")], [KeyboardButton(text="/button_1"), KeyboardButton(text="/button2"),
                                                 KeyboardButton(text="/button3")]]
    panel = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return panel


async def get_card_panel(url):
    panel = InlineKeyboardMarkup(row_width=3, inline_keyboard=[[InlineKeyboardButton(text='Add to card',
                                                                                     web_app=WebAppInfo(url=url))]])
    return panel
