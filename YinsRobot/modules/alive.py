import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/7e2c64c1258218a2ef62a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ɴᴏɪʀ.** \n\n"
  TEXT += "✨ **I'm Working Properly** \n\n"
  TEXT += f"✨ **My Master : [lora](https://t.me/mahalora)** \n\n"
  TEXT += f"✨ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ    :** `{telever}` \n\n"
  TEXT += f"✨ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ   :** `{tlhver}` \n\n"
  TEXT += f"✨ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ✨**"
  BUTTON = [[Button.url("Help", "https://t.me/NoirPunyaBot?start=help"), Button.url("Channel", "https://t.me/stayhall4l2")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
