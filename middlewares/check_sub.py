from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from handlers import user_commands
from aiogram import Dispatcher, F
from aiogram import Router
from aiogram.types import CallbackQuery

dp = Dispatcher()
router = Router()

from keyboards.inline import sub_channel


class CheckSubscription(BaseMiddleware):
    async def __call__ (self, handler, event, data) -> Any:
        channels = ["@newlifenewwaifu", "@uradenegki", "@shesmylife"]
        user_id = event.from_user.id

        if isinstance(event, CallbackQuery) and event.data == 'check':
            for channel in channels:
                chat_member = await event.bot.get_chat_member(channel, user_id)
                if chat_member.status == 'left':
                    await event.answer(
                        'Подпишись на все каналы, чтобы пользоваться ботом!',
                        reply_markup=sub_channel
                    )
                    return

            await check_subs(event)
            return

        return await handler(event, data)

@dp.callback_query(F.data == 'check')
async def check_subs(callback: CallbackQuery):
    await callback.answer("Спасибо за подписки!")

