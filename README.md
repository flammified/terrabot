Terrabot
=====

Introduction
-----
[![PyPI version](https://badge.fury.io/py/terrabot.svg)](https://badge.fury.io/py/terrabot)

Terrabot is a Terraria bot API written in Python.
It is designed to be easy to use and uses the event-listener pattern.

Installation
------

Install the python using pip:

```
pip3 install terrabot
```

Current features
------

 - Connecting to servers
 - Sending chat messages
 - Parsing world data
 - Drawing the world to an image
 - Responding to various events

Missing features
-------

 - Movement
 - The implementation of a lot of packets


Examples
-------

The following is a very basic bot, which will connect and handle chat.

-----
```python
from terrabot import TerraBot
from terrabot.events import Events

#Create a TerraBot object
bot = TerraBot('127.0.0.1')
event = bot.get_event_manager()

#Connect a function to an event using a decorator
@event.on_event(Events.Chat)
def chat(event_id, msg):
    #Do something with the message
    #In this case, stop the bot if the word "Stop" occurs
    print(msg)
    if "stop" in msg:
        bot.stop()

#Start the bot
bot.start()

#And wait
while bot.running:
pass
```

The TerraBot runs in a separate daemon thread. This means that when the main thread is gone, the bot will automatically stop. This is why the example waits for bot.running to become False.
