#Funcion para imprimir las funciones de manera estiulizada
def print_function(func):
    print(func , " = " , eval(func))

#Funcion para verificar si el input es un numero
def numEnt():
    correcto = False
    num = 0
    while (correcto != True):
        try:
            num = int(input("Ingrese el número de la opción que desea: "))
            correcto = True
        except ValueError:
            print("No ingreso un numero")
    return num


#Numeros lambda 0 - 9
zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
four = lambda f: lambda x: f(f(f(f(x))))
five = lambda f: lambda x: f(f(f(f(f(x)))))
six = lambda f: lambda x: f(f(f(f(f(f(x))))))
seven = lambda f: lambda x: f(f(f(f(f(f(f(x)))))))
eight = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))
nine = lambda f: lambda x: f(f(f(f(f(f(f(f(f(x)))))))))


#funciones variadas
alpha = lambda x: x + 1
beta = lambda x: 2*x
f = lambda x: x + 1

'''#funciones lambda para operaciones
    a partir de aqui solo se puede utilizar los numeros lambda'''
sucesor = (lambda n: lambda f: lambda x: f(n(f)(x)))
suma = (lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x)))
producto = (lambda m: lambda n:lambda f: lambda x: n(m(f))(x))
potencia = (lambda m: lambda n: (m)(n))



salir = False
opcion = 0

while (salir != True):

    print("\nBienvenido al menu :")
    print("1. Mostrar los numeros lambda")
    print("2. Mosstrar la funcion sucesor para cada numero lambda")
    print("3. Mostrar la funcion de suma")
    print("4. Mostrar la funcion de producto")
    print("5. Mostrar la funcion de potencia")
    print("6. Funcion alpha")
    print("7. Funcion betha")
    print("8. Salir")


    opcion = numEnt()
    if opcion == 1:
        print("Mostrando cada numero lambda")
        print_function("zero(f)(0)")
        print_function("one(f)(0)")
        print_function("two(f)(0)")
        print_function("three(f)(0)")
        print_function("four(f)(0)")
        print_function("five(f)(0)")
        print_function("six(f)(0)")
        print_function("seven(f)(0)")
        print_function("eight(f)(0)")
        print_function("nine(f)(0)")
    
    elif opcion == 2:
        print("Mostrando la funcion sucesor para cada numero lambda")
        print_function("sucesor(zero)(f)(0)")
        print_function("sucesor(one)(f)(0)")
        print_function("sucesor(two)(f)(0)")
        print_function("sucesor(three)(f)(0)")
        print_function("sucesor(four)(f)(0)")
        print_function("sucesor(five)(f)(0)")
        print_function("sucesor(six)(f)(0)")
        print_function("sucesor(seven)(f)(0)")
        print_function("sucesor(eight)(f)(0)")
        print_function("sucesor(nine)(f)(0)")
    
    elif opcion == 3:
        print("Mostrando la funcion para la suma")
        print_function("suma(six)(nine)(f)(0)")
    elif opcion == 4:
        print("Mostrando la funcion para el producto")
        print_function("producto(six)(nine)(f)(0)")
    elif opcion == 5:
        print("Mostrando la funcion para la potencia")
        print_function("potencia(three)(two)(f)(0)") #aquí el primer numero el exponente y el segundo la base
    elif opcion == 6:
        print("Funcion alpha")
        x = int(input("Ingrese el numero para la funcion alpha: "))
        print_function("alpha(x)")
    elif opcion == 7:
        print("Funcion beta")
        x = int(input("Ingrese el numero para la funcion beta: "))
        print_function("beta(x)")
    elif opcion == 8:
        print('Gracias por utilizar el programa!')
        salir = True
    else:
        print("Ingrese una opcion valida")
        










