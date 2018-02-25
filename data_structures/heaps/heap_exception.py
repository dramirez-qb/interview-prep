class Error(Exception):
    pass


class EmptyHeapError(Error):
    def __init__(self, message):
        self.message = message
