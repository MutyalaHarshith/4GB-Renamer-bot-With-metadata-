"""
Apache License 2.0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import aiohttp, asyncio, warnings, pytz, datetime
import logging
import logging.config
import glob, sys, importlib, pyromod
from pathlib import Path

import pyrogram.utils
from pyrogram import Client, __version__, errors
from pyrogram.raw.all import layer

from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler('BotLog.txt'), logging.StreamHandler()]
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
        
        app_runner = aiohttp.web.AppRunner(await web_server())
        await app_runner.setup()
        bind_address = "0.0.0.0"
        await aiohttp.web.TCPSite(app_runner, bind_address, Config.PORT).start()
        
        path = "plugins/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem.replace(".py", "")
                plugins_path = Path(f"plugins/{plugin_name}.py")
                import_path = "plugins.{}".format(plugin_name)
                spec = importlib.util.spec_from_file_location(import_path, plugins_path)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["plugins" + plugin_name] = load
                print("Imported " + plugin_name)
                
        print(f"{me.first_name} is started")

        for id in Config.ADMIN:
            if Config.STRING_SESSION:
                try:
                    await self.send_message(id, f"2GB+ file support enabled.\nNote: Telegram Premium string session is required.\n\n**__{me.first_name} is started__**")                                
                except: pass
            else:
                try:
                    await self.send_message(id, f"2GB- file support enabled.\n\n**__{me.first_name} is started__**")                                
                except: pass
                    
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} restarted!__**\n\n📅 Date: `{date}`\n⏰ Time: `{time}`\n🌐 Timezone: `Asia/Kolkata`\n\n🉐 Version: `v{__version__} (Layer {layer})`")                                
            except:
                print("Please make this bot an admin in your log channel.")

    async def stop(self, *args):
        for id in Config.ADMIN:
            try: await self.send_message(id, "**Bot stopped.**")                                
            except: pass
        print("Bot stopped.")
        await super().stop()

bot_instance = DigitalRenameBot()

def main():
    async def start_services():
        if Config.STRING_SESSION:
            await asyncio.gather(
                app.start(),
                bot_instance.start()
            )
        else:
            await asyncio.gather(bot_instance.start())
            
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    loop.run_forever()

if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    try:
        main()
    except errors.FloodWait as ft:
        print(f"Flood Wait occurred, sleeping for {ft}")
        asyncio.sleep(ft.value)
        print("Now ready to deploy!")
        main()
