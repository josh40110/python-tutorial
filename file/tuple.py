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