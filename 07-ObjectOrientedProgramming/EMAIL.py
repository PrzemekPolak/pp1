from message import *
class Email(Message):
    def __init__(self, adres_nadawcy, adres_odbiorcy, temat, message):
        self.adres_nadawcy = adres_nadawcy
        self.adres_odbiorcy = adres_odbiorcy
        self.temat = temat
        super().set_message(message)

    def send(self):
        print('Wysyłanie emaila...')
        print(f'Od:    {self.adres_nadawcy}')
        print(f'Do:    {self.adres_odbiorcy}')
        print(f'Temat: {self.temat}')
        print(f'Treść: {self.message}')