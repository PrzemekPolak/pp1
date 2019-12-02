class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
        
    def set_name(self, new_name):
        self.name = new_name
    
    def print_name(self):
        print(self.name)
        
    def set_fullname(self,new_fullname):
        self.fullname = new_fullname
        
    def print_fullname(self):
        print(self.fullname)

x = University()
x.print_fullname()
x.set_fullname('Inna pełna nazwa')
x.print_fullname()

