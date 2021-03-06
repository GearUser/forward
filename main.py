# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Channel-Auto-Post-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FROM_CHANNELS = set(int(x) for x in ("-1001544005690").split())
TO_CHAT = int("-1001650670895")

# filters for auto post
FILTER_TEXT = True
FILTER_AUDIO = True
FILTER_DOCUMENT = True
FILTER_PHOTO = True
FILTER_STICKER = True
FILTER_VIDEO = True
FILTER_ANIMATION = True
FILTER_VOICE = True
FILTER_VIDEO_NOTE = True
FILTER_CONTACT = True
FILTER_LOCATION = True
FILTER_VENUE = True
FILTER_POLL = True
FILTER_GAME = True

FayasNoushad = Client(
    "Channel Auto Post Bot",
    bot_token = "5594361666:AAHhCAkw7Qt_Q7wLsasA31ZYzyPV1VIiO20"
    api_id = "3845818"
    api_hash = "95937bcf6bc0938f263fc7ad96959c6d"
)

START_TEXT = """
Hello {}, I am a channel auto post telegram bot.

Made by @FayasNoushad
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Source Code', url='https://github.com/FayasNoushad/Channel-Auto-Post-Bot')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(
    filters.channel & (
        filters.text if FILTER_TEXT else None |
        filters.audio if FILTER_AUDIO else None |
        filters.document if FILTER_DOCUMENT else None |
        filters.photo if FILTER_PHOTO else None |
        filters.sticker if FILTER_STICKER else None |
        filters.video if FILTER_VIDEO else None |
        filters.animation if FILTER_ANIMATION else None |
        filters.voice if FILTER_VOICE else None |
        filters.video_note if FILTER_VIDEO_NOTE else None |
        filters.contact if FILTER_CONTACT else None |
        filters.location if FILTER_LOCATION else None |
        filters.venue if FILTER_VENUE else None |
        filters.poll if FILTER_POLL else None |
        filters.game if FILTER_GAME else None
    )
)
async def autopost(bot, update):
    if (not update.chat.id in FROM_CHANNELS) or (not TO_CHAT) or ((update.chat.id in FROM_CHANNELS) and (not TO_CHAT)):
        return
    try:
        await update.copy(chat_id=TO_CHAT)
    except Exception as error:
        print(error)
