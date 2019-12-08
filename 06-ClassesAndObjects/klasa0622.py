class termometr():
    def __innit__(self):
        self.temperatura = 36.6
        self.zalaczony = False

    def zalacz(self):
        self.zalaczony = True

    def wylacz(self):
        self.zalaczony = False

    def pomiar_temperatury(self):
        if self.zalaczony:
            import random
            losowa = random.randrange(340, 421)
            self.temperatura = losowa/10

    def wyswietl(self):
        if self.zalaczony:
            print(f'Zmierzona temperatura: {self.temperatura} ', end='')
            if self.temperatura >= 37.0 and self.temperatura < 41.0:
                print('(gorączka)')
            elif self.temperatura >= 41.0:
                print('Stan zagrożenia życia!!!')
                