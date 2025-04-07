import asyncio
from Lyka.misc import SUDOERS
from pyrogram import filters
from Lyka import app
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from Lyka import app
from Lyka.utils.Lyka_ban import admin_filter
from Lyka.utils.database import get_assistant

links = {}


@app.on_message(
    filters.group
    & filters.command(["userbotjoin", f"userbotjoin@{app.username}"])
    & ~filters.private
)
async def join_group(client, message):
    chat_id = message.chat.id
    userbot = await get_assistant(message.chat.id)
    userbot_id = userbot.id
    done = await message.reply("**Please wait inviting assistant**...")
    await asyncio.sleep(1)
    # Get chat member object
    chat_member = await app.get_chat_member(chat_id, app.id)

    # Condition 1: Group username is present, bot is not admin
    if (
        message.chat.username
        and not chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**✅ Assistant Joined.**")
        except Exception as e:
            await done.edit_text("**I need admin power to unban invite my assistant!**")

    # Condition 2: Group username is present, bot is admin, and Userbot is not banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**✅ Assistant Joined.**")
        except Exception as e:
            await done.edit_text(str(e))

    # Condition 3: Group username is not present/group is private, bot is admin and Userbot is banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.RESTRICTED,
        ]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("**ᴀssɪsᴛᴀɴᴛ ɪs ᴜɴʙᴀɴɴɪɴɢ...**")
                await userbot.join_chat(message.chat.username)
                await done.edit_text(
                    "**Assistant was banned, But now unbanned, and joined chat ✅**"
                )
            except Exception as e:
                await done.edit_text(
                    "**Failed to join, Please give ban power and invite user power and invite user power or unban assistant manually then try again by /userbotjoin**"
                )
        return

    # Condition 4: Group username is not present/group is private, bot is not admin
    if (
        not message.chat.username
        and not chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        await done.edit_text("**I need admin power to invite my assistant.**")

    # Condition 5: Group username is not present/group is private, bot is admin
    if (
        not message.chat.username
        and chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        try:
            try:
                userbot_member = await app.get_chat_member(chat_id, userbot.id)
                if userbot_member.status not in [
                    ChatMemberStatus.BANNED,
                    ChatMemberStatus.RESTRICTED,
                ]:
                    await done.edit_text("**✅ Assistant already joined.**")
                    return
            except Exception as e:
                await done.edit_text("**Please wait inviting assistant**.")
                await done.edit_text("**Please wait inviting assistant**...")
                invite_link = await app.create_chat_invite_link(
                    chat_id, expire_date=None
                )
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("**✅ Assistant joined successfully.**")
        except Exception as e:
            await done.edit_text(
                f"**➻ Actually i found that my assistant has not join this group and i am not able to invite my assistant because [ I dont have invite user admin power ] So please provide me invite users admin power then try again by- /userbotjoin.**\n\n**➥ ID »** @{userbot.username}"
            )

    # Condition 6: Group username is not present/group is private, bot is admin and Userbot is banned
    if (
        not message.chat.username
        and chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.RESTRICTED,
        ]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text(
                    "**Assistnat is unbanned**\n**Type again:- /userbotjoin.**"
                )
                invite_link = await app.create_chat_invite_link(
                    chat_id, expire_date=None
                )
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text(
                    "**Assistant was banned, Now unbanned, and joined chat✅**"
                )
            except Exception as e:
                await done.edit_text(
                    f"**➻ Actually i found that my assistant is banned in this group amd am not able to unban my assistant because [ I dont have ban power ] So please provide me ban power or unban my assistant manually then try again by- /userbotjoin.**\n\n**➥ ID »** @{userbot.username}"
                )
        return


@app.on_message(filters.command("userbotleave") & filters.group & admin_filter)
async def leave_one(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        await userbot.leave_chat(message.chat.id)
        await app.send_message(
            message.chat.id, "**✅ Userbot successfully left this chat.**"
        )
    except Exception as e:
        print(e)


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **Userbot** leaving all chats !")
    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001733534088:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"**Userbot leaving all groups...**\n\n**Left :** {left} chats.\n**Failed :** {failed} chats."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"**Userbot leaving...**\n\n**Left :** {left} chats.\n**Failed :** {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"**✅ Left from :* {left} chats.\n**❌ Failed in :** {failed} chats.",
        )
