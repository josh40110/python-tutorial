colors = ['black','white']
sizes = ['L','M','S']
tshirts = [(color,size) for color in colors for size in sizes]
tshirts

symbols = '^%$#&#%$#&#'
tuple(ord(symbol)for symbol in symbols)
listcomp =[ord(symbol)for symbol in symbols]

import array
array.array('I',(ord(symbol)for symbol in symbols))