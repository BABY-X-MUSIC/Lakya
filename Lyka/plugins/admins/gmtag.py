from Lyka import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "Good Night 🌚",
           "Chup chap so ja 🙊",
           "Phone rakh kar so ja, nahi to bhoot aa jayega..👻",
           "Aww babu sona din me kar lena abhi so jao.. 🥲",
           "Mummy dekho ye apne gf se baat kr rha h razai me ghus kar, so nahi raha 😜",
           "Papa ye dekho apne bete ko raat bhar phone chala rha hai 🤭",
           "Jaanu aaj raat ka scene bna le.. 🌠",
           "Gn Sweet dreams Tc.. 🙂",
           "Good night sweet dreams take care.. ✨",
           "Raat bahut ho gyi hai so jao, Gn.. 🌌",
           "Mummy dekho 11 bajne wale hai ye abhi tak phone chala raha hai so nahi raha 🕦",
           "Kal subah school nahi jana kya, jo abhi tak jag rahe ho 🏫",
           "Babu, good night sweet tc 😊",
           "Aaj bahut thand hai, araam se jaldi so jati hoon 🌼",
           "Janeman, good night ",
           "Me ja rahi sone, good night sweet dreams tc 🏵️",
           "Hello ji namaste, good night 🍃",
           "Hey, baby kkrh..? Sona nahi hai kya ☃️",
           "Good night ji, bahut raat ho gayi ⛄",
           "Me ja rahi rone, I mean sone good night ji 😁",
           "Macchli ko kehte hai fish, Good night dear mat karna miss, ja rahi sone 🌄",
           "Good night brightfull night 🤭",
           "The night has fallen, the day is done,, the moon has taken the place of the sun 😊",
           "May all your dreams come true ❤️",
           "Good night sprinkles sweet dream 💚",
           "Good night, Nind aa rhi hai 🥱",
           "Dear friend good night 💤",
           "Baby aaj raat ka scene bna le 🥰",
           "Itni raat me jaag kar kya kar rhe ho sona nahi hai kya 😜",
           "Close your eyes snuggle up tight,, and remember that angels, will watch over you tonight... 💫",
           ]

VC_TAG = [ "Good morning, kese ho 🐱",
         "Gm, subah ho gyi uthna nahi hai kya 🌤️",
         "Gm baby, chai pi lo ☕",
         "Jaldi utho, school nahi jana kya 🏫",
         "Gm, chup chap bister se utho vrna paani daal dungi 🧊",
         "Baby utho aur jaldi fresh ho jao, nasta ready hai 🫕",
         "Office nahi jana kya ji aaj, abhi tak uthe nahi 🏣",
         "Gm dost, coffee/tea kya loge ☕",
         "Baby 8 bajne wale hai, aur tum abhi tak uthe nahi 🕖",
         "Kumbhkaran ki aulad uth jaa ☃️",
         "Good morning have a nice day... 🌄"
         "Good morning, have a good day... 🪴",
         "Good morning, how are you baby 😇",
         "Mummy dekho ye nalayak abhi tak so rha hai... 😵‍💫",
         "Raat bhar babu sona kr rhe the kya, jo abhi tk so rhe ho uthna nahi hai kya... 😏",
         "Baby good morning uth jao aur group me sab friends ko gm wish kro... 🌟",
         "Papa ye abhi tak utha nahi, school ka time nikalta ja rha hai... 🥲",
         "Janeman good mornint, kya kr rhe ho ... 😅",
         "Gm bestiie, breakfast hua kua... 🍳",
        ]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ This command only for groups.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ You are not admin baby, only admins can tag members.")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall Good morning tyle like this / reply any message next time bot tagging...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall Good morning type like this / reply any message next time for tagging...")
    else:
        return await message.reply("/tagall Good morning type like this / reply any message next time bot tagging...")
    if chat_id in spam_chats:
        return await message.reply("๏ Please at first stop running mention process...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ This command only for groups.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ You are not admin baby, only admins can tag members. ")
    if chat_id in spam_chats:
        return await message.reply("๏ Please at first stop running mention process...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ Currently am not tagging baby.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ You are not admin baby, only admins can tag members.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ Process stopped successfully ๏")


