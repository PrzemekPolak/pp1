from json import dumps

komputer = {
    'kolor' : 'czarny',
    'procesor' : 'intel',
    'marka' : 'acer',
    'karta graficzna' : 'geforce',
    'cena' : 3000 
}

new_text = dumps(komputer)

with open('komputer.json','w') as file:
    file.write(new_text)