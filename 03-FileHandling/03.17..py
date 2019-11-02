import re
tekst = 'To be, or not to be, that is the question'

sam = re.findall('[eyuioa]',tekst)

print(f'Liczba samogłosek: {len(sam)}')
