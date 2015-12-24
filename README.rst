Terrabot
========

Introduction
------------

|PyPI version|

Terrabot is a Terraria bot API written in Python. It is designed to be
easy to use and uses the event-listener pattern.

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

+-------+
| \`\`\ |
| `pyth |
| on    |
| from  |
| terra |
| bot   |
| impor |
| t     |
| Terra |
| Bot   |
| from  |
| terra |
| bot.e |
| vents |
| impor |
| t     |
| Event |
| s     |
+-------+
| #Crea |
| te    |
| a     |
| Terra |
| Bot   |
| objec |
| t     |
| bot = |
| Terra |
| Bot(' |
| 127.0 |
| .0.1' |
| )     |
| event |
| =     |
| bot.g |
| et\_e |
| vent\ |
| _mana |
| ger() |
+-------+
| #Conn |
| ect   |
| a     |
| funct |
| ion   |
| to an |
| event |
| using |
| a     |
| decor |
| ator  |
| @even |
| t.on\ |
| _even |
| t(Eve |
| nts.C |
| hat)  |
| def   |
| chat( |
| event |
| \_id, |
| msg): |
| #Do   |
| somet |
| hing  |
| with  |
| the   |
| messa |
| ge    |
| #In   |
| this  |
| case, |
| stop  |
| the   |
| bot   |
| if    |
| the   |
| word  |
| "Stop |
| "     |
| occur |
| s     |
| print |
| (msg) |
| if    |
| "stop |
| "     |
| in    |
| msg:  |
| bot.s |
| top() |
+-------+
| #Star |
| t     |
| the   |
| bot   |
| bot.s |
| tart( |
| )     |
+-------+
| #And  |
| wait  |
| while |
| bot.r |
| unnin |
| g:    |
| pass  |
| \`\`\ |
| `     |
+-------+
| More  |
| examp |
| les   |
| can   |
| be    |
| found |
| under |
| the   |
| 'exam |
| ples' |
| direc |
| tory. |
| Also  |
| check |
| the   |
| wiki  |
| for   |
| more  |
| infor |
| matio |
| n     |
| about |
| the   |
| inner |
| worki |
| ngs   |
| of    |
| the   |
| bot   |
| and   |
| how   |
| to    |
| inter |
| face  |
| with  |
| it.   |
+-------+
| Contr |
| ibuti |
| ng    |
+-------+

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
