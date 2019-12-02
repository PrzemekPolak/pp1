class tv():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        else:
            if len(self.channels) >= self.channel_no:
                print(f'Telewizor jest załączony, kanał {self.channel_no} ({self.channels[self.channel_no - 1]})')
            else:
                print(f'Telewizor jest załączony, kanał {self.channel_no}')
                
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self,channels_list):
        self.channels.extend(channels_list)
        
    def show_channels(self):
        lp = 0
        print('LISTA KANAŁÓW:')
        for x in self.channels:
            lp += 1
            print(f'{lp}. {x}')
        
telewizor = tv()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.show_channels()
telewizor.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'TVN24', 'TVP Info'])
telewizor.show_channels()
telewizor.show_status()
telewizor.set_channel(5)
telewizor.show_status()
telewizor.set_channel(6)
telewizor.show_status()
telewizor.set_channel(9)
telewizor.show_status()
telewizor.set_channel(7)
telewizor.show_status()
telewizor.off()
telewizor.show_status()

