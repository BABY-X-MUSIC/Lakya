import asyncio
import importlib

from pyrogram import idle

import config
from Lyka import LOGGER, app, userbot
from Lyka.core.call import Lyka
from Lyka.misc import sudo
from Lyka.plugins import ALL_MODULES
from Lyka.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "String session not filled, Please fill a Pyrogram V2 Session 🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Lyka.plugins" + all_module)
    LOGGER("Lyka.plugins").info("All features loaded baby 🥳...")
    await userbot.start()
    await Lyka.start()
    await Lyka.decorators()
    LOGGER("Lyka").info("♨️ GrayBots♨️\n")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Lyka").info("♨️ GrayBots♨️")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
