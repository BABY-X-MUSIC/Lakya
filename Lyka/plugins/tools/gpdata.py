from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from Lyka import app
from config import OWNER_ID
from pyrogram.types import Message
from Lyka.utils.Lyka_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("pin") & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**This command works only on groups !**")
    elif not replied:
        await message.reply_text("**Reply to a msg to pin it !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**Successfully pinned msg!**\n\n**Chat:** {chat_title}\n**Admin:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 Views Msg ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**No Pinned Msg found**")
    try:        
        await message.reply_text("Here is the latest pinned msg",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 View Msg",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**This command works only on groups !**")
    elif not replied:
        await message.reply_text("**Reply to a msg to unpin it !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**Successfully unpinned msg!**\n\n**Chat** {chat_title}\n**Admin:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 Views Msg ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**Processing....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**This command work on groups !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**Successfully removed profile photo from group !\nBy** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**The user most need change info admin rights to remove group photo !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("setphoto")& admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("Processing...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`This command work on groups !`") 
      elif not reply:
           await msg.edit("**Reply to a photo or document.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**Sucessfully new profile photo insert !\nBy** {}".format(message.from_user.mention))
             else:
                await msg.edit("**Something wrong happened try another photo !**")
     
          except:
              await msg.edit("**The user most need change info admin rights to change group photo !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("settitle")& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("Processing...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**This command work on groups !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**Sucessfully new group name insert !\nBy** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**The user most need change info admin rights to change group title !**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**Sucessfully new group name insert !\nBy** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**The user most need change info admin rights to change group title !**")
          

    else:
       await msg.edit("**You need reply to text or give some text to change group title **")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("setdiscription") & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**Processing...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**This command works on groups!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**Successfully new group discription insert!**\nBy {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**The user must have change info admin rights to change group description!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**Successfully new group discription insert!**\nBy {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**The user must have change info admin rights to change group description!**")
    else:
        await msg.edit("**You need to reply to text or give some text to change group discription**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("lg")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**Successfully Hiro !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #


