from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



sub_channel = InlineKeyboardMarkup(
    inline_keyboard =[
        [
            types.InlineKeyboardButton(text="1", url="https://t.me/newlifenewwaifu"),
            types.InlineKeyboardButton(text="2", url="https://t.me/uradenegki"),
            types.InlineKeyboardButton(text="3", url="https://t.me/shesmylife"),
            types.InlineKeyboardButton(text="Подписался", callback_data="check")
        ],
    ]
   

)


