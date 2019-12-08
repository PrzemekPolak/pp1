class ksiazka():
    def __init__(self, title, autor, pages, current_page):
        self.title = title
        self.autor = autor
        self.pages = pages
        self.current_page = current_page
        self.opened = False
        
    def open(self):
        self.opened = True

    def close(self):
        self.opened = False

    def show_status(self):
        if self.opened:
            print(f'"{self.title}"  {self.autor}\nStrona: {self.current_page}/{self.pages}')
        else:
            print(f'{self.title}  {self.autor}\nIlość stron: {self.pages}')

    def next_page(self):
        if self.opened and self.current_page == self.pages:
            print('Koniec książki!')
        elif self.opened and self.current_page < self.pages:
            self.current_page += 1
            print(f'Strona {self.current_page}')
        else:
            print('Książka jest zamknięta')

    def previous_page(self):
        if self.opened:
            self.current_page -= 1
            print(f'Strona {self.current_page}')
        else:
            print('Książka jest zamknięta')
