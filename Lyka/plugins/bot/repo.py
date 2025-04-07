from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Lyka import app
from config import BOT_USERNAME
from Lyka.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ Welcome to Lyka Robot 

❥ Bot with awsome features
│❍ • Music + Management •
│❍ • Best Quality Music Sound •
│❍ • No Lag + No Ads •
│❍ • 24x7 Online Support •
├──────────────

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 Add Me Baby 💠", url=f"https://t.me/LykaRobot?startgroup=true")
        ],
        [
          InlineKeyboardButton("✰ Support ✰", url="https://t.me/GrayBotSupport"),
          InlineKeyboardButton("✰ Gray Bots ✰", url="https://t.me/GrayBots"),
          ],
               [
                InlineKeyboardButton("Other Bots", url=f"https://t.me/GrayBots"),
],
[
InlineKeyboardButton("Check", url=f"https://t.me/LevyMusic"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/8605773e8f0c97967ba30-ce204db451bb4ad1e4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
