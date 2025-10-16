#Entradas y salidas
#Maria Isabel Duran Garcia
#TI23110031
#Materia: ASYSC

#Formateo elegante de salidas-en este codigo se nos da varias formas de dar a
# una salida

s = 'Hola Mundo'

str (s)
repr (s)

print("\n")

str(1/7)
x = 10 * 3.25
y = 200 * 200
ss = 'El valor de x es ' + repr(x) + ', y es ' + repr(y)+ '...'
print(ss)

hola = 'hola mundo\n'
holas = repr(hola)
print(holas)
repr((x, y, ('carne', 'huevos')))

#1ra manera para crear una tabla
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ')
    print(repr(x * x * x) .rjust(4))

#2da menera para elaborar tablas
for y in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}' .format (y, y * y, y * y * y))

#El numero en las llaves son la posision de un objeto - este programa toma los objetos
# y los pone en su posision correspondiente
print ('{0} y {1}' .format('carne', 'huevos'))
print ('{1} y {0}'.format('carne', 'huevos'))

#Esta linea de codigo hace una impresion por argumentos
print ('Esta {comida} es {adjetivo}.' .format (comida = 'carne', adjetivo='espantosa'))

#Uso de aplicacion de .format en operaciones matematicas
import math
print('El valor de Pi es aproximadamente {}.' .format(math.pi))
print ('El valor de Pi es aproximadamente {0:.3f}.' .format(math.pi))

#Elabora uan tabla separando los nombres y los numeros ademas anadiendo formato
tabla = {'Sjoerd': 4127, 'Jack':4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}' .format(nombre, telefono))

#Viejo formato de cadenas

print('El valor de pi es aproximadamente %5.3f.' % math.pi)

#Leyendo y escribiendo archivos
#Aqui se utilizara w para escribir un archivos
f = open('archivodetrabajo', 'rb+')
f.write(b'123456abcdefg')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)
f.close()
f.read()