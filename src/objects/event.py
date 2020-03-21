# event is either request or update
class Event:
    def __init__(self, obj, is_request):
        self.request = None
        self.update = None
        self.filed_at = obj.filed_at
        if is_request:
            self.request = obj
        else:
            self.update = obj
