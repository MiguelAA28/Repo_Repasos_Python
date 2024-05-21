# String Data Type

mystring = 'This is a string.'
print(mystring)

print(type(mystring))

print(mystring + 'is of the data type' + str(type(mystring)))


primerstring = 'water'
segundostring = 'fall'
tercerstring = primerstring + segundostring

print(tercerstring)

name = input ('Cual es su nombre?')
print(name)

color = input('cual es su color favorito?')
animal = input('cual es su animal favorito')

print('{}, es como un {} {}!'. format(name, color, animal))
