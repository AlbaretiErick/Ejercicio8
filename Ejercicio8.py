from Clase import Conjunto

if __name__ == '__main__':
    A = Conjunto (lista=[0, 1, 3, 5, 6, 8, 10])
    B = Conjunto (lista=[0, 2, 4, 5, 7, 9, 10])
    A.mostrar ()
    B.mostrar ()
    print ('\nSeleccione una de las siguientes operaciones marcando la letra indicada:\na - Realizar la union de los conjuntos\nb - Calcular A - B\nc - Verificar si los conjuntos son iguales.')
    opcion = input ('Opción: ')
    if opcion == 'a':
        C = A + B
        C.mostrar ()
    elif opcion == 'b':
        C = B - A
        C.mostrar ()
    elif opcion == 'c':
        if A == B:
            print ('\nLos conjuntos A y B son iguales.')
        else:
            print ('\nLos conjuntos A y B no son iguales')
    else:
        print ('\nLa opción seleccionada no existe.')
    print ('\nFin del programa...')