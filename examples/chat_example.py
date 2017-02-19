from terrabot import TerraBot
from terrabot.events import Events

# Create a TerraBot object
bot = TerraBot('192.168.200.231')
event = bot.get_event_manager()


# Connect a function to an event using a decorator
@event.on_event(Events.Chat)
def chat(event_id, msg):
    # Do something with the message
    # In this case, stop the bot if the word "Stop" occurs
    print(msg)
    if "stop" in msg:
        bot.stop()


# Start the bot
bot.start()

# And wait
while bot.client.running:
    pass
