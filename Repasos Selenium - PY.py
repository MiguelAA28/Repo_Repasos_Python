#Format

b, c, d = 6, 75.8, "tal vez"
print("{} {} {} {} {} {} {}". format("el valor es", b, "las opciones", c, "y", d, "son descartables"))

a = "este es el primer parrafo"
b = "este es el segundo parrafo"

print( a + b)

print("-------------------------------------------------------------------------------------------------------")


#Repaso de Listas, Tuplas, Diccionarios para Selenium Python
#LISTAS

print(type(d))

Valores = [1, 2, 3, 5, 56, 4.56]

print(Valores[4])

print(Valores[2 : 5])

Valores.append(25)

print(Valores)

print(Valores[-5])

Valores.insert(2, "lista de valores")

print(Valores)

del Valores[1]

print(Valores)

Valores[3] = 521478

print(Valores)

print("--------------------------------------------------------------------------------------------------------")

#TUPLAS

Vales = (2, 6, "tuplas", 6805)

print(type(Vales))

#Los valores no pueden ser reemplazados

print(Vales)

print("---------------------------------------------------------------------------------------------------------")

#Diccionarios

Diccionario = {}

Diccionario[1] = "casas"
Diccionario[2] = "animales"
Diccionario[3] = "juguetes"
Diccionario[4] = "herramientas"

print(Diccionario)

print(Diccionario[2])

Diccionario[3] = "otros objetos"

print(Diccionario)

print("---------------------------------------------------------------------------------------------------------")

#CONDISIONALES
# IF

Mujer = 25
Hombre = 31

if Mujer > Hombre:
    print("Interesante")
else:
    Mujer < Hombre
    print("Aburrido")

print("----------------------------------------------------------------------------------------------------------")


# Bucle FOR

Listas = [1, 2, 3, 4, 5, 6, 7]

for i in Listas:
    print(i*2)

    


for x in range(1, 10, 5):
    print(x)




for j in range (1, 100):
    print(j)




sumatoria = 0

for i in range(1, 10):
    sumatoria = sumatoria + i
    print(sumatoria)

print("---------------------------------------------------------------------------------------------------------------------------")
  
# WHILE

Num = 0

while Num < 20:
    Num = Num + 1
    if Num == 10:
        break
    print(Num)

print("Final del bucle")


print("-------------------------------------------------------------------------------------------------------------")

#Funciones

def Funci_basic(a, b):
    if a + b >= 10:
        print("Bienvenido al Programa Basico")
    elif a + b < 10 and a + b > 5:
        print("Quizas lo podamos considerar")
    else: 
        a + b == 5 and a + b < 5
        print("Lo sentimos, no es posible que pueda acceder al Programa Basico")

    

print(Funci_basic(1, 3))


print("---------------------------------------------------------------------------------------------------------")


# Clases y Herencias

class Vehiculos:
    def __init__(self, color, forma):
        self.color = color
        self.forma = forma

    def correr(self, mensaje):
        print(mensaje)


Ferrari = Vehiculos("rojo", "cuadrado")

print("el automovil ferrari es de color", Ferrari.color, "y", "tiene forma", Ferrari.forma)

Ferrari.correr("Ademas corre a una velocidad de 320km/h")


class Vehiculos_Agua(Vehiculos):
    def navegar(self, mensaje):
        print(mensaje)

Buque_turismo = Vehiculos_Agua("Blanco", "Obalado")

print("El nuevo buque de la empresa es de color", Buque_turismo.color, "y", "su forma es", Buque_turismo.forma)

Buque_turismo.navegar("Navega a una velocidad de 800 nudos")


print("-----------------------------------------------------------------------------------------------------------")

# EXCEPCIONES (FALLAS EN FUNCIONES DETERMINADAS DENTRO DEL CODIGO)

def Abrir_archivo():
        file = open("battle enter remind umbrella erode.txt")
        print(file.read())
        try:
            return print(file.read())
        except: FileNotFoundError
        finally: 
            print("No se puso encontrar el archivo TXT deseado")


print("---------------------------------------------------------------------------------------------------------")



















    


