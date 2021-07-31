#(©)Codexbotz

import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait... \n ■■■■■■□90%")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔰 JOIN MOVIE REQUEST GROUP 🔰", url="https://t.me/NEW_MLM_HD_MOVES"),
                ],[
                    InlineKeyboardButton("💢 ALL MOVIES 💢", url="https://t.me/mlm_movie_1"),
                    InlineKeyboardButton("💢 NEW MOVIES 💢", url="https://t.me/MLM_ROKES")
                ],[
                    InlineKeyboardButton("🔰 JOIN UPDATE CHANNEL 🔰", url="https://t.me/mlm_movies_update"),
                ],[
                    InlineKeyboardButton("CLOSE ❎", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    text = "<b>SORRY..!\n ഞാൻ all movies എന്ന ചാനെലിൽ നിന്നാണ് സിനിമ തരുന്നത് നിങൾ all movies ചാനെലിൽ ജോയിൻ ചെയ്താലേ എനിക്ക് സിനിമ തരാൻ കഴിയൂ..\n ദയവായി ALL MOVIES ചാനെലിൽ ജോയിൻ ചെയ്ത ശേഷം ഗ്രൂപ്പിലെ ലിങ്കിൽ പോയി ഒന്ന് കൂടെ വന്ന് start കൊടുക്കൂ..😊\nJOIN : @MLM_MOVIE_1</b>"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>and <a href='https://t.me/{client.username}?start={argument}'>try again</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup(
        [
            [
               InlineKeyboardButton("💢ALL MOVIES💢", url = client.invitelink)
            ],[
               InlineKeyboardButton("💢ALL MOVIES💢", href ="https://t.me/{client.username}?start={argument}")
            ]
        ]
    )
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )
