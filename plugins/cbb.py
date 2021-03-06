#(Β©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>π ADMIN ONLY COMMANDS π \n\n /start - start the bot or get posts \n\n /batch - create link for more than one posts \n\n /genlink - create link for one post \n                  β’βββ β½ β’ β½ ββββ’ \n\nβ CREATOR : <a href='tg://user?id={OWNER_ID}'>This Person</a>\nβ LANGUAGE : <code>Python3</code>\nβ LIBRARY : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nβ SOURCE CODE : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a> \nβTHANKS TO :CODEXBOTZ</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("β Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
