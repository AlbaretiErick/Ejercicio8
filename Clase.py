class Conjunto:
    __numeros = []
    def __init__(self, lista):
        self.__numeros = lista
    def __add__ (self, conjunto):
        for i in self.__numeros:
            j = 0
            while j<len (conjunto.__numeros) and i!=conjunto.__numeros[j]:
                j = j + 1
            if j>=len (conjunto.__numeros):
                conjunto.__numeros.append (i)
        return conjunto
    def __sub__ (self, conjunto):
        for i in self.__numeros:
            j = 0
            while j<len (conjunto.__numeros) and i!=conjunto.__numeros[j]:
                j = j + 1
            if j<len (conjunto.__numeros):
                conjunto.__numeros.pop (j)
        return conjunto
    def __eq__ (self, conjunto):
        bul = True
        for i in self.__numeros:
            j = 0
            while j<len (conjunto.__numeros) and i!=conjunto.__numeros[j]:
                j = j + 1
            if j>=len (conjunto.__numeros):
                bul = False
        return bul
    def mostrar (self):
        print (self.__numeros)