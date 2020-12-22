import csv
from Nodo import Nodo
from colorama import Fore, Back, Style
import threading
from colorama import init
from dibujarGrafo import Dibujar

init(autoreset=True)

from BusquedasCiegas import *
from BusquedasHeuristicas import *

class Grafo():
    def __init__(self):
        self.nodos = []

    def eliminarNodos(self):
        self.nodos=[]

    def crearGrafo1(self,archivo,dib):
        with open(archivo, newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                nodoA=self.getNodoByStr(str(row[0]))
                if nodoA is None:
                    nodoA=self.addNode(str(row[0]))

                    nodoA.setValor(row[1])
                    dib.addNode(nodoA.getNombre(),nodoA.getValor())
                nodoB=self.getNodoByStr(str(row[2]))
                if nodoB is None:
                    nodoB=self.addNode(str(row[2]))

                    nodoB.setValor(row[3])
                    dib.addNode(nodoB.getNombre(),nodoB.getValor())
                self.addArista(nodoA,nodoB,row[4])
                dib.addEdge(nodoA.getNombre(),nodoB.getNombre(),row[4])

    def crearGrafo(self,archivo):
        with open(archivo, newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                nodoA=self.getNodoByStr(str(row[0]))
                if nodoA is None:
                    nodoA=self.addNode(str(row[0]))
                    nodoA.setValor(row[1])
                nodoB=self.getNodoByStr(str(row[2]))
                if nodoB is None:
                    nodoB=self.addNode(str(row[2]))
                    nodoB.setValor(row[3])
                self.addArista(nodoA,nodoB,row[4])

    def crearGrafoBi(self,archivo):
        with open(archivo, newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                nodoA=self.getNodoByStr(str(row[0]))
                if nodoA is None:
                    nodoA=self.addNode(str(row[0]))
                    nodoA.setValor(row[1])

                nodoB=self.getNodoByStr(str(row[2]))
                if nodoB is None:
                    nodoB=self.addNode(str(row[2]))
                    nodoA.setValor(row[3])

                if(nodoA.conectaA(nodoB)==False):
                    self.addArista(nodoA,nodoB,row[4])
                    self.addArista(nodoB, nodoA, row[4])

    def crearGrafoHe(self,archivo):
        with open(archivo, newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if(str(row[0]) != ''):
                    nodoA=self.getNodoByStr(str(row[0]))
                    if nodoA is None:
                        nodoA=self.addNode(str(row[0]))
                        nodoA.setValor(row[1])
                    else:
                        nodoA.setValor(row[1])
                if(str(row[2]) != ''):
                    nodoB=self.getNodoByStr(str(row[2]))
                    if nodoB is None:
                        nodoB=self.addNode(str(row[2]))
                        nodoB.setValor(row[3])

                    if(nodoA.conectaA(nodoB)==False):
                        self.addArista(nodoA,nodoB,row[4])


    def addArista(self, nodoA, nodoB, peso):
        nodoA.addArista(nodoB,peso)
    def getNodos(self):
        return self.nodos;
    def getNodoByStr(self, name):
        for i in self.nodos:
            if i.getNombre() == name:
                return i
        else:
            return None;
    def addNode(self, name):
        nodo = Nodo(name)
        self.nodos.append(nodo)
        return nodo
    def __str__(self):
        j=[]
        for i in self.nodos:
            j.append(i.getNombre())
        return j
    def validarDestinos(self,destinos): #Retorna un array de Nodos correspondientes al array de strings
        vectorDestinos=[]
        for i in destinos:
            nodo = self.getNodoByStr(i)
            if (nodo is not None):
                vectorDestinos.append(nodo)
        return vectorDestinos
    def Amplitud(self,origen,destinos):
        #destinos array de strings
        nodoA=self.getNodoByStr(origen)
        if(destinos=='' and nodoA is not None):
            Busqueda().AmplitudSF(nodoA)
        else:
            vectorDestinos=self.validarDestinos(destinos)
            if(nodoA is not None and len(vectorDestinos)>0):
                Busqueda().Amplitud(nodoA,vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")
    def Profundidad(self, origen,destinos):
        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):
            Busqueda().ProfundidadSF(nodoA)
        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                Busqueda().Profundidad(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")

    def ProfundidadIterativa(self,origen,destinos):
        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):
            nodoB=Nodo('asd')
            Busqueda().ProfundidadIterativa(nodoA,[nodoB.getNombre()])
            print(Fore.CYAN+'Grafo recorrido en su totalidad')
        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                Busqueda().ProfundidadIterativa(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")
    def Bidireccional(self,nodoAstr,nodoBstr):
        nodoA=self.getNodoByStr(nodoAstr)
        nodoB=self.getNodoByStr(nodoBstr)
        if (nodoA is not None and nodoB is not None):
            Busqueda().Bidireccional(nodoA,nodoB)
        else:
            print('¡error! Los nodos ingresados no existen en el grafo')
    def CostoUniforme(self,origen,destinos):
        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):

            Busqueda().costoUniformeSF(nodoA)
            print(Fore.CYAN + 'Grafo recorrido en su totalidad')

        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                Busqueda().costoUniforme(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")

    def AscensoColina(self,origen,destinos):
        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):
            BusquedaH().AscensoColinaSF(nodoA)
        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                BusquedaH().AscensoColina(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")

    def PrimeroMejor(self,origen,destinos):
        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):
            nodoB = Nodo('asd')
            BusquedaH().PrimeroMejor(nodoA,[nodoB.getNombre()])
            print(Fore.CYAN + 'Grafo recorrido en su totalidad')
        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                BusquedaH().PrimeroMejor(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")

    def Aestrella(self,origen,destinos):

        nodoA = self.getNodoByStr(origen)
        if (destinos == '' and nodoA is not None):
            nodoB = Nodo('asd')
            BusquedaH().Aestrella(nodoA,[nodoB.getNombre()])
            print(Fore.CYAN + 'Grafo recorrido en su totalidad')
        else:
            vectorDestinos = self.validarDestinos(destinos)
            if (nodoA is not None and len(vectorDestinos) > 0):
                BusquedaH().Aestrella(nodoA, vectorDestinos)
            else:
                print("¡ERROR! Alguno de los datos ingresados no existen en el grafo")

def menu():
    print(Fore.GREEN+"#########################################")
    print(Fore.GREEN+"#\t\t\t\tBUSQUEDAS\t\t\t\t#")
    print(Fore.GREEN+"#########################################\n")
    print(Fore.GREEN+'--------------A CIEGAS-------------------')
    print(Fore.GREEN+'1. Amplitud')
    print(Fore.GREEN+'2. Amplitud (TODO)')
    print(Fore.GREEN+'3. Profundidad')
    print(Fore.GREEN+'4. Profundidad (TODO)')
    print(Fore.GREEN+'5. Profundidad Iterativa')
    print(Fore.GREEN+'6. Profundidad Iterativa (TODO)')
    print(Fore.GREEN+'7. Costo Uniforme')
    print(Fore.GREEN+'8. Costo Uniforme (TODO)')
    print(Fore.GREEN+'9. Bidireccional')

    print(Fore.GREEN+'--------------HEURISTICAS----------------')
    print(Fore.GREEN+'10. Ascenso a la colina')
    print(Fore.GREEN+'11. Primero el mejor')
    print(Fore.GREEN+'12. Primero el mejor (TODO)')
    print(Fore.GREEN+'13. A*')
    print(Fore.GREEN+'14. A* (TODO)')
    print(Fore.RED+'\nq. Salir')
    opc = input("\n>>>")
    return opc
def dibujar():
    dib = Dibujar()
    grafo.crearGrafo1(archivo,dib)
    print('entra')
    dib.dibujar()

grafo = Grafo()
archivo="prueba3.csv"

origen='S'
destinos=['E']
destinoBi='E'

hilo1 = threading.Thread(target=dibujar)
hilo1.start()

opc=menu()
while (opc!='q'):

    if (opc == '1'):
        grafo.crearGrafo(archivo)
        grafo.Amplitud(origen,destinos)
        grafo.eliminarNodos()

    elif (opc == '2'):
        grafo.crearGrafo(archivo)
        grafo.Amplitud(origen,'')
        grafo.eliminarNodos()

    elif (opc == '3'):
        grafo.crearGrafo(archivo)
        grafo.Profundidad(origen,destinos)
        grafo.eliminarNodos()

    elif (opc == '4'):
        grafo.crearGrafo(archivo)
        grafo.Profundidad(origen,'')
        grafo.eliminarNodos()

    elif (opc == '5'):
        grafo.crearGrafo(archivo)
        grafo.ProfundidadIterativa(origen,destinos)
        grafo.eliminarNodos()

    elif (opc == '6'):
        grafo.crearGrafo(archivo)
        grafo.ProfundidadIterativa(origen,'')
        grafo.eliminarNodos()

    elif (opc == '7'):
        grafo.crearGrafo(archivo)
        grafo.CostoUniforme(origen, destinos)
        grafo.eliminarNodos()

    elif (opc == '8'):
        grafo.crearGrafo(archivo)
        grafo.CostoUniforme(origen,'')
        grafo.eliminarNodos()

    elif (opc=='9'):
        grafo.crearGrafoBi(archivo)
        grafo.Bidireccional(origen, destinoBi)
        grafo.eliminarNodos()

    elif (opc == '10'):
        grafo.crearGrafoHe(archivo)
        grafo.AscensoColina(origen,destinos)
        grafo.eliminarNodos()
    elif (opc == '11'):
        grafo.crearGrafoHe(archivo)
        grafo.PrimeroMejor(origen, destinos)
        grafo.eliminarNodos()
    elif (opc == '12'):
        grafo.crearGrafoHe(archivo)
        grafo.PrimeroMejor(origen, '')
        grafo.eliminarNodos()

    elif (opc == '13'):
        grafo.crearGrafoHe(archivo)
        grafo.Aestrella(origen, destinos)
        grafo.eliminarNodos()
    elif (opc == '14'):
        grafo.crearGrafoHe(archivo)
        grafo.Aestrella(origen, '')
        grafo.eliminarNodos()

    input('\npulse una tecla para continuar ')
    opc = menu()



#grafo.crearGrafo('prueba.csv')

#grafo.ProfundidadIterativa('H',['J'])

#print(grafo.__str__())
#print(grafo.getNodos()[0].getAristasStr())

#for i in grafo.getNodos():
#    print(i.getAristasStr())
#grafo.Bidireccional('H','M')
# #grafo.costoUniforme('I',['M'])





