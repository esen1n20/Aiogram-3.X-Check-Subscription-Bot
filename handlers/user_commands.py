from aiogram import Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Dispatcher, F, types
from middlewares.check_sub import CheckSubscription
from aiogram.types import CallbackQuery

import keyboards

from keyboards import inline

dp = Dispatcher()
router = Router()

@router.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(f"Для продолжения подпишись на каналы.", reply_markup = inline.sub_channel)







