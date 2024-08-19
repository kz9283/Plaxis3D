class ObservableModel:
    def __init__(self):
        self._event_listeners = {}

    def add_event_listener(self, event, func):
        try:
            self._event_listeners[event].append(func)
        except KeyError:
            self._event_listeners[event] = [func]
            
        return lambda: self._event_listeners[event].remove(func)

    def trigger_event(self, event):
        if event not in self._event_listeners.keys():
            return
        for func in self._event_listeners[event]:
            func(self)

