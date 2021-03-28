import pandas as pd
Data = {'10 hombres mas ricos del mundo en el 2020, lista de Forbes': ['Jeff Bezos', 'Bernard Arnault y su familia', 'Elon Musk', 'Bill Gates', 'Mark Zuckerberg', 'Warrem Buffett', 'Larry Ellison',
'Larry Page', 'Amancio Ortega', 'Sergey Brin'],
            'Edad': ['55 años', '71 años', '48 años', '65 años', '36 años', '90 años', '76 años', '47 años', '84 años', '47 años'],
            'Fortuna': ['186.500 millones de dolares', '142.100 millones de dolares', '132.100 millones de dolares', '119.300 millones de dolares', '102.000 millones de dolares', '87.400 millones de dol
ares', '78.900 millones de dolares', '78.700 millones de dolares', '76.900 millones de dolares', '76.500 mmillones de dolares']}
frame = pd.DataFrame(Data)
frame