class Message():
    def __init__(self):
        self.message = ''

    def set_message(self,message):
        x = message 
        x2 = x.lower()
        x3 = x2.capitalize()
        x3 += ' BYE.'
        self.message = x3
