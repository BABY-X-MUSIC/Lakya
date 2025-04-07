from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ChatGPT", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("Quotly", callback_data="mplus HELP_Q"),InlineKeyboardButton("Stickers", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("Tag-all", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Github", callback_data="mplus HELP_Github"),InlineKeyboardButton("Extra", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("Action", callback_data="mplus HELP_Action"),InlineKeyboardButton("Search", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("Font", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Couples", callback_data="mplus HELP_Couples"),InlineKeyboardButton("T-graph", callback_data="mplus HELP_TG")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
