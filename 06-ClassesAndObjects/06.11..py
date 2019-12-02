class tv():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        else:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')

telewizor = tv()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()


