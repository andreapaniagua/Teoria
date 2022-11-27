import os
import time

def celdas(first, second):
    #Para ir analizando los elementos será necesario crear las celdas para la tabla
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res

def gramatica(file="./grammar.txt"):
    #Se leeran los elementos de la gramatica del lenguaje de un .txt

    #Para esto sera necesario separar los elementos terminales, de los no terminales y las variables
    #basandose en los signos -> y |. Ademas de las combinaciones entre elementos
    #gracias a que python es capaz de diferenciar entre mayusculas y minusculas

    file = os.path.join(os.curdir, file)
    with open(file) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []
        for rule in rules:
            left, right = rule.split(" -> ")
            right = right[:-1].split(" | ")
            for ri in right:
                if str.islower(ri):
                    t_rules.append([left, ri])
                else:
                    v_rules.append([left, ri])
        return v_rules, t_rules

def input(file="./input.txt"):
    #La lectura del input necesita ser capaz de leer todo el string que se desea analizar
    #separando las palabras por medio de los espacios en blanco

    file = os.path.join(os.curdir, file)
    res = []
    with open(file) as inp:
        inputs = inp.readlines()
        for i in inputs:

            # remove \n

            res.append(i[:-1].split())
    return res


def cyk_alg(varies, terms, inp):

    #Para la funcion del algoritmo será necesario medir el tiempo de ejecucion
    
    #Sera necesario ingresar el input tras haber removido los espacios en blanco y haber separado el string en palabras 

    startT = time.time()
    length = len(inp)
    
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]

    #La tabla esta conformada por los sets de elementos que leidos de la gramatica 

    table = [[set() for _ in range(length-i)] for i in range(length)]

    for i in range(length):
        for te in terms:
            if inp[i] == te[1]:
                table[0][i].add(te[0])

    #Se llena la tabla de manera iterativa mediante la funcion de crear celdas anteriormente
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = celdas(table[k][j], table[i-k-1][j+k+1])
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])

    # if the last element of table contains "S" the input belongs to the grammar
    #Si el ultimo elemento en la tabla contiene el elemento S, significa que el input si es posible formar la palabra 
    endT = time.time()
    print(f"Tiempo de ejecución: {j} {(endT- startT)*10**3:.03f}ms")
    return table


def result(tab, inp):
    #Para mostrar los elementos en la tabla se tomaran algunas libertades, 
    #Primero, si el elemento no tiene pertenencia en la gramatica, se coloca un guión
    #Tras haber colocado cualquier elemento, se coloca una sangría entre las celdas
    #En caso de que si haya un elemento a colocar, entonces se imprime y luego se agrega la sangría
    #En caso de que cumpla con las condiciones, se imprimirá un texto informando al usuario.

    for c in inp:
        print("\t{}".format(c), end="\t")
    print()
    for i in range(len(inp)):
        print(i+1, end="")
        for c in tab[i]:
            if c == set():
                print("\t{}".format("_"), end="\t")
            else:
                print("\t{}".format(c), end=" ")
        print()

    if 'S' in tab[len(inp)-1][0]:
        print("El input es parte de la gramatica")
    else:
        print("El input no forma parte de esta gramatica")
        
    

    


if __name__ == '__main__':
    v, t = gramatica()

    r = input()[0]
    
    ta = cyk_alg(v, t, r)
    
    result(ta, r)

