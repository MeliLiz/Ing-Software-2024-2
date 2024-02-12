
# Montañas y valles
#Contar valles
def valles():

    seguir = True
    while seguir:
        cadena = input("Ingrese la cadena de pasos: ")
        seguir = False
        for i in cadena:
            if i != 'D' and i != "U":
                print("Cadena no valida")
                seguir = True

    valles = 0
    contador = 0
    estado = False

    for i in cadena:
        if contador < 0:
            estado = True
        else:
            estado = False

        if i == 'D':
            contador -= 1
        else:
            contador +=1

        if contador == 0 and estado == True:
            valles += 1
            estado = False

    print("Numero de valles: " + str(valles))


# Arbol ordenado
class arbol:

    class nodo:
        def __init__(self, valor):
            if valor is None:
                valor = 0
            self.valor = valor
            self.der = None
            self.izq = None
            self.padre = None

    def __init__(self):
        self.raiz = None

    def add(self, val):
        if val is None:
            val = 0

        if self.raiz is None:
            self.raiz = self.nodo(val)
        else:
            self.add2(self.raiz, val)

    def add2(self, nodo, valor):
        actual = nodo
        if valor <= actual.valor :
            if actual.izq is None:
                nuevo = self.nodo(valor)
                actual.izq = nuevo
                nuevo.padre = actual
            else:
                actual = actual.izq
                self.add2(actual, valor)
        else:
            if actual.der is None:
                nuevo = self.nodo(valor)
                actual.der = nuevo
                nuevo.padre = actual
            else:
                actual = actual.der
                self.add2(actual, valor)

    def preorden(self): #raiz, izquierdo, derecho
        recorrido = []
        return self.preorden1(self.raiz, recorrido)

    def preorden1(self, nodo, recorrido):
        if nodo is not None:
            recorrido.append(nodo.valor)
            self.preorden1(nodo.izq, recorrido)
            self.preorden1(nodo.der, recorrido)

        return recorrido

    def inorden(self): #derecho, raiz, izquierdo
        recorrido = []
        return self.inorden1(self.raiz, recorrido)

    def inorden1(self, nodo, recorrido):
        if nodo is not None:
            self.inorden1(nodo.izq, recorrido)
            recorrido.append(nodo.valor)
            self.inorden1(nodo.der, recorrido)

        return recorrido

    def postorden(self): #derecho, izq, raiz
        recorrido = []
        return self.postorden1(self.raiz, recorrido)

    def postorden1(self, nodo, recorrido): # derecho, izquierdo, raiz
        if nodo is not None:
            self.postorden1(nodo.izq, recorrido)
            self.postorden1(nodo.der, recorrido)
            recorrido.append(nodo.valor)

        return recorrido


if __name__ == "__main__":
    arbol = arbol()
    arbol.add(5)
    arbol.add(3)
    arbol.add(8)
    arbol.add(1)
    arbol.add(4)

    print(arbol.postorden())

    valles()