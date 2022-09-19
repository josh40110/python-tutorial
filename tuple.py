#Example 2-7. Tuples used as records
lax_coorinates =(33.9425,-118.408056)
city ,year ,pop ,chg , area = ('Tokyo', 2003 , 32450 ,0.66 ,8014)
traveler_ids =[('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country , _ in traveler_ids:
    print(country)
'''
line 3 A list of tuples of the form (country_code, passport_number)
line 5 The % formatting operator understands tuples and treats each item as a separate field
line 6 The for loop knows how to retrieve the items of a tuple separately—this is called
“unpacking.” Here we are not interested in the second item, so it’s assigned to
_, a dummy variable
'''

#Tuple Unpacking (also called iterable unpacking)
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # tuple unpacking
latitude
longitude

#prefixing an argument with a star
divmod(20,8) #divmod return(a//b , a%b)
t= (20,8)
divmod(*t)
quotient ,reminder = divmod(*t)
quotient,reminder

# _as placeholder
import os

import numpy
_,filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
filename #os.path.split() function builds a tuple (path, last_part) from a filesystem path
#Sometimes when we only care about certain parts of a tuple when unpacking, a dummy variable like _ is used as placeholder

#using * to grab excess items , * can appear in any position
a, b, *rest = range(5)
a, b, rest
a, *b, rest = range(3)
a, b, rest
*a, b, rest = range(2)
a, b, rest
*a, b, rest = range(5)
a, b, rest

# Nested Tuple Unpacking

metro_areas   = [('Tokyo','JP',36.933,(35.689722,139.691997)),
('Delhi NCR ', 'IN', 21.935,(28.613889,772.208889)),
('Mexico City'  ,'MX',20.142 , (19.433333 , -99.133333)), 
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9} | {:^9}'
for name , cc ,pop , (latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))


#Named Tuple
#Example 2-9. Defining and using a named tuple type

from collections import  namedtuple
City = namedtuple('City',['name','country','population','coordinates'])
# City = namedtuple('City','name country population coordinates')
tokyo  =City('Tokyo','JP',36.933,(35.689722,139.691667))
tokyo
tokyo.coordinates
tokyo[2]
# line 64 two parameters given class name , list of field name. which can be given as an iterable of strings or as a single spacedelimited string

#Example 2-10. Named tuple attributes and methods (continued from the previous example)
City._fields 
LatLong = namedtuple('LatLong', 'lat long') #純(a,b)被視為tuple nametuple 被視為一個instance (__main__.City)
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
#if I do City('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889)) is same as City._make(delhi_data) 
delhi = City._make(delhi_data) #City(*delhi_data) let tuple namedtuple
delhi = delhi._asdict()  #_asdict為namedtuple的under function
for key, value in delhi.items():
    print(key + ':', value)
delhi_data
delhi

#Slicing Example 2-11. Line items from a flat-file invoice
    

invoice = """
... 0.....6.................................40........52...55........
... 1909 Pimoroni PiBrella                    $17.50 3 $52.50
... 1489 6mm Tactile Switch x20               $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201                $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240               $34.95 1 $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

test = numpy.array([[1,3,4,5],[1,3,5,6],[2,234,3234]])
type(test[0,...])

#Assigning to Slices
l = list(range(10))
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
l
[0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
l
[0, 1, 20, 11, 5, 22, 9]

l[2:5] = 100 # When the target of the assignment is a slice, the right side must be an iterable object, even if it has just one item.
# so it doesn't work

l[2:5] = [100]
l
[0, 1, 100, 22, 9]

hasattr([100],'__iter__')

my_list = [['1','3']]*3 
#*數值："裡面"層*3
# for i in range："同層"*3 
my_list

#Building list of lists
#Example 2-12. A list with three lists of length 3 can represent a tic-tac-toe board
#過三關
board = [['_'] *3] *3
board  
board[1][2] = ['0']
board  

row=['_'] * 3
board = []
for i in range(3):
    board.append(row)
board[1][2] = '0'
board


board = [['_'] *3  for i in range(3)]
board
board[1][2] = '0'
board
#*=+= __iadd__ and __add__
l = [1,2]
id(l)
l =  l *2
id(l)
l*=2
id(l)

t=(2,3)
id(t)
t*=2
t
id(t)

import dis
#Example 2-15. The unexpected result: item t2 is changed and an exception is raised
t = (1, 2, [30, 40])
dis.dis('t[2] += [50, 60]')
t
# t[2].extend([50,60]) can work
