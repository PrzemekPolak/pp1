from message import *
class Sms(Message):
    def __init__(self, telefon_nadawca, telefon_odbiorca, tresc):
        self.telefon_nadawca = telefon_nadawca
        self.telefon_odbiorca = telefon_odbiorca
        super().set_message(tresc) 

    def send(self):
        print('Wysyłanie SMSa...')
        print(f'Od:    {self.telefon_nadawca}')
        print(f'Do:    {self.telefon_odbiorca}')
        print(f'Treść: {self.message}')
