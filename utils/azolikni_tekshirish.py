from typing import Union

from aiogram import Bot


async def tekshirish(user_id,kanal_link:Union[str,int]):
    bot = Bot.get_current()
    chek = await bot.get_chat_member(chat_id=kanal_link,user_id=user_id)
    return chek.is_chat_member()
