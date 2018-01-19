print('import empty stack module')

class Error(Exception):
    pass

class EmptyStackError(Error):
    def __init__(self, message):
        self.message = message
