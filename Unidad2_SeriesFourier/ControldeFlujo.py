#Herramientas para Control de Flujo
#Maria Isabel Duran Garcia
#TI23110031
#Materia: ASYSC

#1. Sentencia If- En este se nos muestra como es la estructura
# base de la sentencia if.

print("sentencia if")

x = int(input("Ingresa un numero por favor: "))

if x < 0:
    x = 0
    print('Negativo cambiado a 0')
elif x == 0:
        print('cero')
elif x == 1:
        print('simple')
else:
        print('Mas')
print("\n")
#2. Sentencia for - Estructura base, este codigo hace un conteo de letras en una 
#cadena de texto
print("Sentencia for\n")

palabras = ['gato', 'ventana', 'defenestrado']

for p in palabras:
    print(p, len(p))
# Para borrar items
for p in palabras[:]:
    if len (p) > 6:
        palabras.insert(0, p)#Hace una copia sobre las palabras
        print(palabras)
print("\n")
#3. Funcion range - Muestra los numeros que estan dentro de un rango

for i in range (5):
    print(i)
#iterar sobre los indeces de una secuencia
print("\n")

a = ['Maria','tenia','un', 'corderito']
for i in range(len(a)):
    print(i, a[i])
#4. Sentencias Break, continue y else en lazos, en este codigo
# se identifican numeros primos usando break, for y else
print("\n")
for n in range (2, 10):
    for x in range (2, n):
        if n % x == 0:
           print(n, 'es igual a', x, '*', n/x) 
           break
    else:
          print(n, 'es un numero primo')
#5. continue en este programa tiene la funcion de dar continuacion a una salida
print("\n")
for num in range(2, 10):
    if num % 2 == 0:
        print("Encontre un numero par", num)
        continue
    print("Encontre un numero", num)
#6. La sentencia pass se usa cuando una sentencia es requerida por la sintaxis
print("\n")
while True:
    pass
#7. Definiendo Funiones, en este codigo se muestra los numeros de la serie
# Fibonacci hasta un limite
print("\n")
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(2000)

#8 Argumentos con vlores por omision----

def pedirConfirmacion(prompt, reintentos = 4, queja = 'Si o no, por favor'):
    while True: 
        ok = input(prompt)
        if ok in ('s','S','si','Si','SI'):
            return True
        if ok in ('n','no', 'No','NO'):
            return False
        reintentos = reintentos -1
        if reintentos < 0:
            raise OSError('usuario no existe')
        print(queja)
        
#En este programa omite un valor ya delarado
print("\n")
i = 5

def f(arg = i):
    print(arg)
i = 6
f()

#palabras clave como argumentos

def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")
loro(1000)                                          # argumento posicional
loro(tension=1000)                                  # argumento nombrado
loro(tension=1000000, accion='VOOOOOM')             # argumentos nombrados
loro(accion='VOOOOOM', tension=1000000)             # argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar')    # args posicionales
loro('mil', estado='viendo crecer las flores desde abajo')

#Lista de argumentos arbitrarios
print("\n")
def concatenar(*args, sep="/"):
    return sep.join(args)
concatenar("Tierra","Marte", "Venus")
print(concatenar)

