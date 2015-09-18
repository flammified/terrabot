class EventManager(object):

    def __init__(self):
        self.event_listeners = {}
        self.event_methods = {}

    """A decorator function
        Use it as follows:

        eventmanager = bot.get_event_manager()

        @eventmanager.on_event(Events.CHAT)
        def chat_message(self, event_id, data):
            print(data)

    """
    def on_event(self, event_id):
        def add_wrapper(f):
            if not event_id in self.event_listeners:
                self.event_listeners[event_id] = []
            self.event_listeners[event_id].append(f)
            return f
        return add_wrapper

    def method_on_event(self, event_id, listener):
        if not event_id in self.event_methods:
            self.event_methods[event_id] = []
        self.event_methods[event_id].append(listener)

    def raise_event(self, event_id, data):
        # print("Event happened: ", event_id)
        if event_id in self.event_listeners:
            for f in self.event_listeners[event_id]:
                f(event_id, data)
        if event_id in self.event_methods:
            for f in self.event_methods[event_id]:
                f(event_id, data)
