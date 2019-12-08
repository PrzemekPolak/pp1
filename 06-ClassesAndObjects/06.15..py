class tv():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.glosnosc = 0
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        else:
            if len(self.channels) >= self.channel_no:
                print(f'Telewizor jest załączony, głośność: {self.glosnosc}, kanał {self.channel_no} ({self.channels[self.channel_no - 1]})')
            else:
                print(f'Telewizor jest załączony, głośność: {self.glosnosc}, kanał {self.channel_no}')
                
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
    
    def zwieksz_glosnosc(self):
        if self.glosnosc != 10:
            self.glosnosc += 1
    
    def zmniejsz_glosnosc(self):
        if self.glosnosc != 0:
            self.glosnosc -= 1
        
telewizor = tv()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.zwieksz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zwieksz_glosnosc()
telewizor.show_status()
telewizor.zwieksz_glosnosc()
telewizor.show_status()
telewizor.zwieksz_glosnosc()
telewizor.show_status()
telewizor.zwieksz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.zmniejsz_glosnosc()
telewizor.show_status()
telewizor.off()
telewizor.show_status()





