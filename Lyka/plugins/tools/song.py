import os

import requests
import yt_dlp
from pyrogram import filters
from youtube_search import YoutubeSearch
from ... import app

from config import SUPPORT_CHAT


def fetch_song(song_name):
    url = f"https://song-teleservice.vercel.app/song?songName={song_name.replace(' ', '%20')}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 and "downloadLink" in response.json() else None
    except Exception as e:
        print(f"API Error: {e}")
        return None

@app.on_message(filters.command("song"))
async def handle_song(client, message):
    song_name = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    if not song_name:
        return await message.reply("Please provide a song name after the /song command..")

    song_info = fetch_song(song_name)
    if not song_info:
        return await message.reply(f"Sorry, I couldn't find the song '{song_name}'.")

    filename = f"{song_info['trackName']}.mp3"
    download_url = song_info['downloadLink']

    # Download and save the file
    with requests.get(download_url, stream=True) as r, open(filename, "wb") as file:
        for chunk in r.iter_content(1024):
            if chunk:
                file.write(chunk)

    caption = (f"""❖ Song name ➥ {song_info['trackName']}\n\n● Album ➥ {song_info['album']}\n ● Release date ➥ {song_info['releaseDate']}\n● Requested by ➥ {message.from_user.mention}\n❖ Powered by  ➥ ˹ Lyka Robot™""")

    # Send audio and clean up
    await message.reply_audio(audio=open(filename, "rb"), caption=caption)
    os.remove(filename)
