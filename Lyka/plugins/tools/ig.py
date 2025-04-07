import re
import requests
from pyrogram import filters

from Lyka import app
from config import LOGGER_ID


@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Please provide the instagram feel URL after command"
        )
        return
    url = message.text.split()[1]
    if not re.match(
        re.compile(r"^(https?://)?(www\.)?(instagram\.com|instagr\.am)/.*$"), url
    ):
        return await message.reply_text(
            "The provided URL is not a valid instagram URL😅😅"
        )
    a = await message.reply_text("Processing...")
    api_url = f"https://insta-dl.hazex.workers.dev/?url={url}"

    response = requests.get(api_url)
    try:
        result = response.json()
        data = result["result"]
    except Exception as e:
        f = f"Eʀʀᴏʀ :\n{e}"
        try:
            await a.edit(f)
        except Exception:
            await message.reply_text(f)
            return await app.send_message(LOGGER_ID, f)
        return await app.send_message(LOGGER_ID, f)
    if not result["error"]:
        video_url = data["url"]
        duration = data["duration"]
        quality = data["quality"]
        type = data["extension"]
        size = data["formattedSize"]
        caption = f"Duration : {duration}\nQuality : {quality}\nType : {type}\nSize : {size}"
        await a.delete()
        await message.reply_video(video_url, caption=caption)
    else:
        try:
            return await a.edit("Failed to download reel")
        except Exception:
            return await message.reply_text("Failed to download reel")


MODULE = "Reel"
HELP = """
Instagram Reel Downloader:

• /ig [URL]: Download instagram reels. Provide the instagram reel URL after the command.
• /instagram [URL]: Download instagram reels. Provide the instagram reel URL after the command.
• /reel [URL]: Download instagram reels. Provide the instagram reel URL after the command.
"""
