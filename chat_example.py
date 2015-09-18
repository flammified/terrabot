from terrabot import TerraBot
from terrabot.events import Events

import threading

bot = TerraBot('127.0.0.1')
event = bot.get_event_manager()

@event.on_event(Events.Chat)
def chat(event_id, msg):
    msg = str(msg, "utf-8")
    print(msg)
    if "stop" in msg:
        bot.stop()

@event.on_event(Events.Blocked)
def cant_connect(event_id, msg):
    print(msg)
    bot.stop()

@event.on_event(Events.TileUpdate)
def tile_update(event_id, tiles):
    print("Tile update")

@event.on_event(Events.Initialized)
def initialized(event_id, data):
    print("Initialized")

@event.on_event(Events.Login)
def logged_in(event_id, data):
    print("Logged in")

bot.start()

while bot.running:
    pass
