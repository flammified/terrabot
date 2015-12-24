Terrabot
========

Introduction
------------

|PyPI version|

| Terrabot is a Terraria bot API written in Python.
| It is designed to be easy to use and uses the event-listener pattern.

Installation
------------

Install the module using pip:

::

    pip3 install terrabot

Current features
----------------

-  Joining servers
-  Chatting
-  Triggering various events, like joining, tiledata and itemdrops
-  Parsing server data to keep classes up-to-date
-  Moving the bot by teleporting

Examples
--------

The following is a very basic bot, which will connect and handle chat.

--------------

.. code:: python

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

More examples can be found under the 'examples' directory. Also check
the wiki for more information about the inner workings of the bot and
how to interface with it.

Contributing
------------

If you want to contribute, that's great! I would really appreciate the
help. Just send a pull request and i'll quickly check and accept it.
These are some areas that need work:

-  NPC packet parsing
-  Item dropping
-  Teleporting other players (>:D)
-  Synchronizing packets like health and update-player-packets
-  Placing tiles (!)

For information about the packets, see `this
link <https://tshock.atlassian.net/wiki/display/TSHOCKPLUGINS/Packet+Documentation>`__.

.. |PyPI version| image:: https://badge.fury.io/py/terrabot.svg
   :target: https://badge.fury.io/py/terrabot
