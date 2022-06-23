import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/dbbb842f911facca0a83e.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ɪᴛsᴜᴋᴀ.** \n\n"
  TEXT += "✨ **DUA TIGA TUTUP BOTOL BACOT KONTOL** \n\n"
  

  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
