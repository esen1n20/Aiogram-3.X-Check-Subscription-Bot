import asyncio
import keyboards



from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from handlers import user_commands
from aiogram import Dispatcher, F, Bot
from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards import inline
from middlewares.check_sub import CheckSubscription
from middlewares import check_sub






bot = Bot("7357468680:AAEOPhPgqcm0VrtxTX5PiX9Qtwr9S2uVgVA")
dp = Dispatcher()
router = Router()

@dp.callback_query(F.data == 'check')
async def check_subs(callback: CallbackQuery):
    await callback.answer("Спасибо за подписки!")

dp.message.middleware(CheckSubscription())

async def main():
    dp.include_routers(
        user_commands.router
    )
    
    
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())