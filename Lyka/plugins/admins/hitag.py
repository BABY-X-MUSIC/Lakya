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

TAGMES = [ "Baby kaha ho 🤗",
           "Oye so gye kya, online aao 😊",
           "Oye VC aao baat krte hai 😃",
           "Khana khaya ya nahi ?",
           "Ghar me sab kaise hai ? 🥺",
           "Pata hai boht yaad aa rhi aapki 🤭",
           "Aur batao kaise ho ? 🤨",
           "Meri bhi setting karwado 🙂",
           "Oye hello aapka naam kya hai ?",
           "Nashta ho gya ? 😋",
           "Mujhe bhi apne private group me add krlo na 😍",
           "VC aao aapka dost aapko bula rha hai 😅",
           "Hello aapki shadi ho gyi kya ? 🤔",
           "Sone chale gye kya ? 🙄",
           "Are yaar koi song play krdo 😕",
           "Aap kaha se ho ? 🙃",
           "Hello ji namaste 😛",
           "Or btao kya kr rhe ho 🤔",
           "Kya aap mujhe jaante ho ?☺️",
           "Aao game khelte hai 🤗",
           "Chalti ho kya 9 se 12 😇",
           "Aapke papa kya krte hai 🤭",
           "Aao chlo golgappe khane chalte hai 🥺",
           "Ghar se bahar mat ghuma kro kidnap ho jaoge 😶",
           "Or btao nashta ho gya ? 🤔",
           "Good morning 😜",
           "Oye hello mera ek kaam karoge 🙂",
           "Dj wale babu mera gaana chala doge ? 😪",
           "Aapse milke accha laga",
           "Mere baabu ne thaana khaya kya ? 🙊",
           "Padhai kesi chal rhi hai ? 😺",
           "Or btao kya kr rhe ho ?",
           "Are tum theek to ho na ? 😅",
           "Tu meri photo click krega ek ? 😅",
           "Are kaha bhaag gye online aao 😆",
           "Aaor bhabhi se kab mila rhe ho 😉",
           "Kya aap mujhse pyaar krte ho ? 💚",
           "Me tumse boht pyaar krti hu 👀",
           "Accha suno na ek kissi dedo na 🙉",
           "Ek joke sunaun kya ? 😹",
           "Vc aao kuch dikhati hun 😻",
           "Kya tum instagram chalate ho ? 🙃",
           "Whatsapp number dena apna 😕",
           "Aapki dost se meri setting krwa do 🙃",
           "Saara kaam ho gya ho to, online aa jao 🙃",
           "Aap kaha se ho 😊",
           "Jaa aaj tujhe mene apne dil se aajad kr diya hai 🥺",
           "Mera ek kaam kroge group me kuch members add krdo ♥️",
           "Me tumse naraaj hu 😠",
           "Aapki family me sab kaise hai ? ❤",
           "Kya hua ..? 🤔",
           "Aao na Vc pr bore ho rhi hun 😒",
           "Bhul gye mujhe ? 😏",
           "Jhut kyu bola aapne mujhse 🤐",
           "Itna bhaw mat khaya kro ROti khao roti 😒",
           "Ye attitude kise dikha rhe ho 😮",
           "Hello kaha busy ho 👀",
           "Aapke jesa dost mushkil se milta hai 🙈",
           "Aaj man boht udaas hai ☹️",
           "Mujhse bhi baat krlo na 🥺",
           "Aaj khane me kya bnaya hai ?👀",
           "Or kya chal rha hai life me 🙂",
           "Msg bhi kr liya kro kabhi kabhi 🥺",
           "Me cute hu na ? 🥺",
           "Kal maja aaya tha na 😅",
           "Kal poora din kaha bsy the 😕",
           "Aap relationship me ho kya..? 👀",
           "Kitne shaant rhte ho aap 😼",
           "Aapko gaana gaan aaata hai..? 😸",
           "Ghumne chaloge mere saath..?? 🙈",
           "Humesha happy rha kro yaar 🤞",
           "Kya hum dost ban skte hai...? 🥰",
           "Aapka vivah ho gya kya.. 🥺",
           "Online aa jaya kro kabhi kabhi dear",
           "Single ho ya mingle 😉",
           "Aao party karte hai 🥳",
           "Vc join krlo aajao 🧐",
           "Me tumse pyaar krti hu 🥺",
           "Vc aao batein krte hai 🤭",
           "Bhul gye ho kya mujhe,..? 😊",
           "Apna bna le piya, apna bana le 🥺",
           "Mera group bhi join krlo 🤗",
           "Mene tera naam dil rakh diya 😗",
           "Tumhare saare dost kha gye 🥺",
           "Admin kon hai yahan ka ? 🥰",
           "Kiski yaadon me khoye rehte ho 😜",
           "Good night ji bohot raat ho gyi hai 🥰",
           ]

VC_TAG = [ "If you do not step forward you will remain in the same place.",
         "Life is Hard but impossible.",
         "Life is too short to argue and fight.",
         "Don't wait for the perfect moment take moment and make it perfect.",
         "Silence is the best answer to someone who doesn't value your words.",
         "Every day is new day is a chance to change your life.",
         "To change your life, You need to change your priorities.",
         "Life is a journey, not a race..",
         "Smile and don't worry, life is awsome.",
         "Do not compare yourself to others if you so so you are insulting yourself.",
         "I am in the process of becoming the best version of myself.",
         "Life is like ice enjoy it before it melts.",
         "Be free like a bird.",
         "No one is coming to save you. This life of your is 100% your responsiblity..",
         "Life always offers you a second chance. It's called tomorrow.",
         "Life begins at the end of your comfort zone.",
         "All the things that hurt you, actually teach you.",
         "Life is like a camera. So face it with a smile.",
         "Life is 10% of what happens to you and 90% of how you respond to it.",
         "Life always offers you a second chance. It's called tomorrow.",
         "No one is coming to save you. This life of your is 100% your responsiblity..",
         "Life is not an easy task.",
         "Life is a wonderfull adventure.",
         "Life begins on the other side of despair.",
         "Life is not a problem to be solved but a reality to be experienced.",
         "Life does not have a remote, Get up and change it yourself.",
         "Start trusting yourself, and you'll know how to live",
         "Health is the most important good of life.",
         "Time change priority changes.",
         "To see and to feel mean to be, think and live.",
         "Be with someone who brings out the best of you.",
         "Your thoughts are your life.",
         "People change, Memories don't.",
         "Our life what we think it is.",
         "Light heart lives longer.",
         "Depression deventually becomes a habit.",
         "Life is a gift. Treat it well.",
         "Life is what our feelings do with us.",
         "Winkles are the lines of life on the face.",
         "Life is made up of sobs, sniffles, and smiles.",
         "Not life, but good life, is to be chiefly valued.",
         "You change your life by changing your heart.",
         "Life is nothing without true friendship.",
         "If you are brave to say good bye, Life will reward you with a new hello.",
         "There is nothing more exciting in the world, but people.",
         "You can do anything, But not everything.",
         "Life become easy when you become strong.",
         "My life isn't perfect but it does have perfect moments.",
         "Life is god's novel. Let him write it.",
         "Our life is a result of our dominant thoughts.",
         "Life is a motion from a desire to another desire.",
         "To live means to fight.",
         "Life is like a mountain, Not a beach.",
         "The worst thing in life is what it passes.",
         "Life is simple if we are simple.",
         "Always think twice, speak once.",
         "Life is simple, we make it complicated.",
         "Life is not much older than the death.",
         "The secret of life is low expectations!",
         "Life is a teacher.., The more we live, The more we learn.",
         "Human life is nothing but ann eternal illusion.",
         "The happier the time, The shorter it is.",
         "Life is beautifull if you know where to look.",
         "Life is awesome with you by my side.",
         "Life - Love = Zero",
         "Life is full of struggles.",
         "I got less but i got best",
         "Life is 10% what you make it, and 90% how you take it.",
         "There is still so much to see",
         "Life doesn't get easier you get stronger.",
         "Life is about laughing & living.",
         "Eachh person dies when his time comes.",
        ]


@app.on_message(filters.command(["hitag" ], prefixes=["/", "@", "#"]))
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
        return await message.reply("๏ You are not admin baby, Only admins can tag memners. ")

    if message.reply_to_message and message.text:
        return await message.reply("/hitag Good morning type like this  / Reply any msg next time bot tagging...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/hitag Good morning type like this  / Reply any msg next time bot tagging...")
    else:
        return await message.reply("/hitag Good morning type like this  / Reply any msg next time bot tagging...")
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


@app.on_message(filters.command(["lifetag"], prefixes=["/", "@", "#"]))
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
        return await message.reply("๏ You are not admin baby, Only admins can tag members. ")
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



@app.on_message(filters.command(["cancel", "histop", "lifestop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ Currently i'm not tagging baby.")
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
        return await message.reply("๏ You are not admin baby, Only admins can tag members.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ Process stopped successfully ๏")
