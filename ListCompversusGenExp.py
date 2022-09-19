colors = ['black','white']
sizes = ['L','M','S']
tshirts_listComprehensive = [(color,size) for color in colors for size in sizes] 
tshirts_listComprehensive #in list comperhensive
for tshirt in ('%s %s'%(c,s)for c in colors for s in sizes):
    print(tshirt) #generator expression


symbols = '^%$#&#%$#&#'
tuple(ord(symbol)for symbol in symbols)
listcomp =[ord(symbol)for symbol in symbols]

import array
array.array('I',(ord(symbol)for symbol in symbols))
#The first argument of the array constructor defines the storage type used for the numbers in the array