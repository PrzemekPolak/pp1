class tv():
    def __init__(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        else:
            print('Telewizor jest załączony')

telewizor = tv()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.off()
telewizor.show_status()


