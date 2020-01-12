class Kolejka():
    def __init__(self):
        self.queue = []

    def add_element(self, new_element):
        self.queue.append(new_element)
        print(f'Dodano: {new_element}')

    def remove_element(self):
        print(f'Usunięto: {self.queue[0]}')
        self.queue.pop(0)

    
kolejka = Kolejka()
kolejka.add_element(1)
kolejka.add_element(2)
kolejka.add_element(3)
kolejka.add_element(4)
kolejka.add_element(5)
kolejka.remove_element()
kolejka.remove_element()
kolejka.remove_element()