from terrabot import TerraBot
from terrabot.events import Events

import threading

bot = TerraBot('127.0.0.1', protocol=156)
eventm = bot.event_manager

@eventm.on_event(Events.Chat)
def chat(event_id, msg):
    print(msg)
    msg = str(msg, "utf-8")
    if "stop" in msg:
        bot.stop()

bot.start()

while threading.active_count() > 1:
   pass
