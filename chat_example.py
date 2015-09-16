from terrabot import TerraBot
from terrabot.events import Events

import threading

bot = TerraBot('127.0.0.1', protocol=155)
eventm = bot.event_manager

@eventm.on_event(Events.Chat)
def chat(event_id, msg):
    msg = str(msg, "utf-8")
    print(msg)
    if "stop" in msg:
        bot.stop()

@eventm.on_event(Events.Blocked)
def cant_connect(event_id, msg):
    print(msg)
    bot.stop()

@eventm.on_event(Events.Login)
def logged_in(event_id, data):
    print("Logged in")

bot.start()

while bot.running:
    pass
