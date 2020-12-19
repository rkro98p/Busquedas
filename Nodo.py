class Nodo():
    def __init__(self, nombre):
        self.nombre=nombre
        self.valor=0
        self.aristas=[]

    def getNombre(self):
        return self.nombre

    def addArista(self,nodoD,peso):
        self.aristas.append(Arista(nodoD,peso))

    def getAristas(self):
        return self.aristas
    def getAristasStr(self):
        j=''
        for i in self.aristas:
            j+=self.nombre+i.__str__()+'\n'
        return  j
    def getValor(self):
        return self.valor
    def setValor (self, valor):
        self.valor=valor

    #Para metodo Profundidad Iterativa
    def setNivel(self, nivel):
        self.nivel = nivel
    def getNivel(self):
        return self.nivel
    def getAristasSN(self, nodoQuitar):
        aux = []
        for i in self.aristas:
            if (i.getNodoDest != nodoQuitar):
                aux.append(i)
        return aux

    def conectaA(self,nodoB):
        for i in self.aristas:
            if(i.getNodoDest()==nodoB):
                return True
        return False


class Arista():
    def __init__(self, nodoDest,peso):
        self.nodoDest=nodoDest
        self.peso=peso

    def getPeso(self):
        return self.peso

    def getNodoDest(self):
        return self.nodoDest
    def __str__(self):
        return '---('+ str(self.peso)+')-->'+self.nodoDest.getNombre()