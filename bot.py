#Apache License 2.0
#Copyright (c) 2022 @AniHorizon 

# extra imports
import aiohttp, asyncio, warnings, pytz, datetime
import logging
import logging.config
import glob, sys, importlib, pyromod
from pathlib import Path
from aiohttp import web  # Fixed import

# pyrogram imports
import pyrogram.utils
from pyrogram import Client, __version__, errors
from pyrogram.raw.all import layer

# bots imports
from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app as rename_app  # Renamed to avoid conflict

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

# Get logging configurations
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler('BotLog.txt'),
              logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class DigitalRenameBot(Client):
    def __init__(self):
        super().__init__(
            name="DigitalRenameBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        self.premium = Config.PREMIUM_MODE
        self.uploadlimit = Config.UPLOAD_LIMIT_MODE

        app_runner = web.AppRunner(await web_server())  # Fixed
        await app_runner.setup()
        await web.TCPSite(app_runner, "0.0.0.0", Config.PORT).start()

        path = "plugins/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem
                plugins_path = Path(f"plugins/{plugin_name}.py")
                import_path = "plugins.{}".format(plugin_name)
                spec = importlib.util.spec_from_file_location(import_path, plugins_path)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules[import_path] = load  # Fixed
                print("Digital Botz Imported " + plugin_name)

        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")

        for id in Config.ADMIN:
            try:
                if Config.STRING_SESSION:
                    await self.send_message(id, f"𝟮𝗚𝗕+ ғɪʟᴇ sᴜᴘᴘᴏʀᴛ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ...\n**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
                else:
                    await self.send_message(id, f"𝟮𝗚𝗕- ғɪʟᴇ sᴜᴘᴘᴏʀᴛ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ...\n**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL,
                                        f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`")
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

    async def stop(self, *args):
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**Bot Stopped....**")
            except:
                pass
        print("Bot Stopped 🙄")
        await super().stop()

bot_instance = DigitalRenameBot()

def main():
    async def start_services():
        tasks = [bot_instance.start()]
        if Config.STRING_SESSION:
            tasks.append(rename_app.start())  # Renamed app used
        await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    loop.run_forever()

if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    try:
        main()
    except errors.FloodWait as ft:
        print(f"Flood Wait Occured, Sleeping For {ft}")
        asyncio.run(asyncio.sleep(ft.value))
        print("Now Ready For Deploying !")
        main()
