import time
import random
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from info import DLT_TIME
from Script import script

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    myrr = await message.reply_sticker("CAACAgEAAx0CarZSAAMZ_2R9icLTN5vSSFuCuYVDX4-Teq7bAAL6AQACjLEgRHhzeIjneBzEHgQ")
    andi = await message.reply_text("ʜᴇʏ ʙᴜᴅᴅʏ ɪ ᴀᴍ ᴀʟɪᴠᴇ 💃\n\nᴄʟɪᴄᴋ /start ꜰᴏʀ ᴍᴏʀᴇ​ 😻")
    await asyncio.sleep(DLT_TIME)
    await myrr.delete()
    await andi.delete()
    await message.delete()
    
@Client.on_message(filters.command("swag", CMD))
async def tutorial(_, message):
    await message.reply_text("😎")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")

