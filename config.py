# Apache License 2.0
# Copyright (c) 2022 @AniHorizon
# Telegram Link : https://t.me/AniHorizon
# Repo Link : https://github.com/MythicMosaic/4GB-Renamer-bot-With-metadata-
# License Link : https://github.com/MythicMosaic/4GB-Renamer-bot-With-metadata-/tree/main/LICENSE

import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):  # AniHorizon client config

    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # premium account string session required
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "cluster0")
    DB_URL = os.environ.get("DB_URL", "")

    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://files.catbox.moe/6afj23.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6705898491').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002283909105"))

    # free upload limit
    FREE_UPLOAD_LIMIT = 6442450944  # 6GB

    # premium mode feature
    UPLOAD_LIMIT_MODE = True
    PREMIUM_MODE = True

    # force subscribe
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", ""))
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Digital_Botz")

    # web response config
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()


class rkn(object):  # part of text configuration

    START_TXT = """<b><blockquote>ʜᴇʏ !! {mention}

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ~ ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏs, ᴍᴏᴠɪᴇs, ᴀɴɪᴍᴇs, ᴏʀ ᴀɴʏ ғɪʟᴇs ʏᴏᴜ sᴇɴᴅ~

ᴊᴜsᴛ sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ᴘɪᴄᴋ ᴀ ɴᴇᴡ ɴᴀᴍᴇ ғᴏʀ ɪᴛ!</blockquote></b>"""

    ABOUT_TXT = """<b><blockquote>
Owner     : <a href='https://t.me/Momo_Ayase_bot'>This Person</a>
Library   : <a href='https://github.com/pyrogram'>Pyrogram</a>
Language  : <a href='https://www.python.org'>Python 3</a>
Updates   : <a href='https://t.me/AniHorizon'>AniHorizon</a>
Paid Bot  : <a href='https://t.me/Tharun_stryker'>REON</a>
Developer : <a href='https://t.me/Momo_Ayase_bot'>STRYKER</a>
</blockquote></b>"""

    HELP_TXT = """
/start - Start the bot.

<b><u>How To Rename A File</u></b>
Send any file and type a new filename. Then select the format [document, video, audio].

ℹ️ For more help, contact: <a href="https://t.me/Momo_Ayase_bot">Support</a>"""

    UPGRADE_PREMIUM = """
⪼ ★Plans    -  ⏳Date - 💸Price
⪼ 🥉Bronze  -   3 days -   39
⪼ 🥈Silver  -   7 days -   59
⪼ 🥇Gold    -  15 days -  99
⪼ 🏆Platinum -  1 month -  179
⪼ 💎Diamond -  2 months -  339

Daily Upload Limit: Unlimited
Discount on All Plans: Rs.9"""

    UPGRADE_PLAN = """
Plan: Pro
Date: 1 month
Price: 179
Limit: 100 GB

Plan: Ultra Pro
Date: 1 month
Price: 199
Limit: 1000 GB

Discount on All Plans: Rs.9"""

    THUMBNAIL = """
🌌 <b><u>How To Set Thumbnail</u></b>

<b>•></b> Send any photo to automatically set thumbnail.
<b>•></b> /del_thumb - Delete your old thumbnail.
<b>•></b> /view_thumb - View your current thumbnail."""

    CAPTION = """
📑 <b><u>How To Set Custom Caption</u></b>

<b>•></b> /set_caption - Set a custom caption.
<b>•></b> /see_caption - View your custom caption.
<b>•></b> /del_caption - Delete your custom caption.

Example: /set_caption 📕 File Name: {filename}   💾 Size: {filesize}   ⏰ Duration: {duration}"""

    BOT_STATUS = """
⚡️ Bot Status ⚡️

⌚️ Uptime: {}
👭 Total Users: {}
💸 Premium Users: {}
֍ Uploads: {}
⊙ Downloads: {}"""

    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    AniHorizon_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

`--change-title @AniHorizon 
--change-video-title @AniHorizon 
--change-audio-title @AniHorizon 
--change-subtitle-title @AniHorizon 
--change-author @AniHorizon `

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Momo_Ayase_bot
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @AniHorizon `
Exᴀᴍᴩʟᴇ:- `/set_prefix @AniHorizon `
"""
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/MythicMosaic/4GB-Renamer-bot-With-metadata-/tree/main</a>

• ❣️ <a href=https://github.com/MythicMosaic>MythicMosaic</a>
• ❣️ <a href=https://github.com/MythicMosaic>AniHorizon</a>
• ❣️ <a href=https://github.com/a2-b3c4d>Stryker</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

`--change-title @AniHorizon 
--change-video-title @AniHorizon 
--change-audio-title @AniHorizon 
--change-subtitle-title @AniHorizon 
--change-author @AniHorizon `

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Momo_Ayase_bot 
"""
    
    Ani_PROGRESS = """<b>\n
╭━━━━❰Ani PROCESSING...❱━➣
┣⪼ 🗃️ ꜱɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ ᴅᴏɴᴇ : {0}%
┣⪼ 🚀 ꜱᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
