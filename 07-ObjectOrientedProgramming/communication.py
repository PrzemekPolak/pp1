from message import *
from SMS import *
from EMAIL import *

sms = Sms('888888888', '444444444', 'Treść smsa.')
email = Email('nadawca@ww.pl', 'odbiorca@ww.pl','Super temat', 'Tresc emaila.')

sms.send()
print('')
email.send()