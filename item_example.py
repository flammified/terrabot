from terrabot import TerraBot
from terrabot.events import Events

bot = TerraBot('127.0.0.1')
event = bot.get_event_manager()

@event.on_event(Events.ItemDropped)
def logged_in(event_id, data):
    print(data)

bot.start()

while bot.running:
    pass
