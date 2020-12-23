from collections import deque
from operator import itemgetter
from colorama import Fore
from colorama import init

from Nodo import Nodo

init(autoreset=True)

import time

def ordenarHijos(hijos):
    hijos = sorted(hijos, key=lambda x: x.getNombre())
    return hijos

##############################
##########AMPLITUD############
##############################
class Busqueda():
    def Amplitud(self, origen,destinos):
        # Inicializar variables
        tic = time.perf_counter()

        cola = deque()
        visitados = []
        extrae = None
        cola.append(origen)
        aux = 0

        print('\n*****************************************')
        print('          BUSQUEDA POR AMPLITUD          ')
        print('*****************************************')
        while (extrae not in destinos):

            if (len(cola) > 0):
                extrae = cola.popleft()
            else:
                print('\nBusqueda terminada, NO se han encontrado caminos para el nodo destino')
                break

            if (extrae not in visitados):
                visitados.append(extrae)
                nodosRel = []
                for i in extrae.getAristas():
                    if (i.getNodoDest() not in visitados and i.getNodoDest() not in cola):
                        nodosRel.append(i.getNodoDest())
                nodosRel = ordenarHijos(nodosRel)
                cola += nodosRel

                print('---------------------')
                print('Extrae:\t\t' + extrae.getNombre())
                print('Cola:\t\t' + ' '.join(x.getNombre() for x in cola))
                aux = aux + 1
            print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))

            if extrae in destinos:
                print('\n¡Nodo encontrado!')

        toc = time.perf_counter()

        print(Fore.CYAN+"Busqueda terminada en "+str((toc-tic)*1000)+'ms')
        #print(Fore.CYAN+f"Busqueda terminada en {toc - tic:0.8f} segundos")

    def AmplitudSF(self, origen):
        # Inicializar variables
        tic = time.perf_counter()

        cola = deque()
        visitados = []
        extrae = None
        cola.append(origen)
        aux = 0

        print('\n*****************************************')
        print('          BUSQUEDA POR AMPLITUD          ')
        print('*****************************************')
        while (len(cola)>0):

            if (len(cola) > 0):
                extrae = cola.popleft()
            #else:
             #  print('\nBusqueda terminada, NO se han encontrado caminos para el nodo destino')
            #    break

            if (extrae not in visitados):
                visitados.append(extrae)
                nodosRel = []
                for i in extrae.getAristas():
                    if (i.getNodoDest() not in visitados and i.getNodoDest() not in cola):
                        nodosRel.append(i.getNodoDest())
                nodosRel=ordenarHijos(nodosRel)
                cola += nodosRel
                print('---------------------')
                #print('Iteracion:' + str(aux))
                print('Extrae:\t\t' + extrae.getNombre())
                print('Cola:\t\t' + ' '.join(x.getNombre() for x in cola))
                aux = aux + 1
            print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))

        toc = time.perf_counter()
        print(Fore.CYAN + '\nGrafo recorrido en su totalidad en '+str((toc-tic)*1000)+ 'ms')
        #print(Fore.CYAN+f"\nGrafo recorrido en su totalidad en {toc - tic:0.8f} segundos")

    def Profundidad(self, origen, destinos):
        # Inicializar variables
        tic = time.perf_counter()

        cola = deque()
        visitados = []
        extrae = None
        cola.append(origen)
        aux = 0

        print('\n*****************************************')
        print('          BUSQUEDA POR PROFUNDIDAD          ')
        print('*****************************************')
        while (extrae not in destinos):

            if (len(cola) > 0):
                extrae = cola.popleft()
            else:
                print('\nBusqueda terminada, NO se han encontrado caminos para el nodo destino')
                break

            if (extrae not in visitados):
                visitados.append(extrae)
                nodosRel = deque()
                for i in extrae.getAristas():
                    if (i.getNodoDest() not in visitados and i.getNodoDest() not in cola):
                        nodosRel.append(i.getNodoDest())
                nodosRel = deque(ordenarHijos(nodosRel))
                cola=nodosRel+cola

                print('---------------------')
                print('Extrae:\t\t' + extrae.getNombre())
                print('Cola:\t\t' + ' '.join(x.getNombre() for x in cola))
                aux = aux + 1
            print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))

            if extrae in destinos:
                print('\n¡Nodo encontrado!')

        toc = time.perf_counter()
        print(Fore.CYAN +'Busqueda terminada en '+ str((toc-tic)*1000)+ 'ms')
        #print(Fore.CYAN+f"Busqueda terminada en {toc - tic:0.8f} segundos")

    def ProfundidadSF(self, origen):
        # Inicializar variables
        tic = time.perf_counter()

        cola = deque()
        visitados = []
        extrae = None
        cola.append(origen)
        aux = 0

        print('\n*****************************************')
        print('          BUSQUEDA POR PROFUNDIDAD          ')
        print('*****************************************')
        while (len(cola)>0):

            if (len(cola) > 0):
                extrae = cola.popleft()
            #else:
             #  print('\nBusqueda terminada, NO se han encontrado caminos para el nodo destino')
            #    break

            if (extrae not in visitados):
                visitados.append(extrae)
                nodosRel = deque()
                for i in extrae.getAristas():
                    if (i.getNodoDest() not in visitados and i.getNodoDest() not in cola ):
                        nodosRel.append(i.getNodoDest())
                #nodosRel = ordenarHijos(nodosRel)
                nodosRel = deque(ordenarHijos(nodosRel))
                cola=nodosRel+cola
                print('---------------------')
                print('Extrae:\t\t' + extrae.getNombre())
                print('Cola:\t\t' + ' '.join(x.getNombre() for x in cola))
                aux = aux + 1
            print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))

        toc = time.perf_counter()
        print(Fore.CYAN +"\nGrafo recorrido en su totalidad en "+str((toc-tic)*1000)+ 'ms')
        #print(Fore.CYAN+f"\nGrafo recorrido en su totalidad en {toc - tic:0.8f} segundos")

    def ProfundidadIterativa(self,origen,destinos):
        tic = time.perf_counter()
        # Inicializar variables
        origen.setNivel(0)
        cola = deque()
        visitados = []
        extrae = None
        cola.append(origen)
        nivel = 0
        aux = 0
        terminar = 0

        print('\n****************************************************')
        print('          BUSQUEDA POR PROFUNDIDAD ITERATIVA       ')
        print('****************************************************')

        while(terminar == 0 and extrae not in destinos ):
            terminar=1
            print("----------Nivel "+str(nivel)+"--------")
            visitados=[]
            aux=0
            while (extrae not in destinos):
                if(nivel==0):
                    terminar=0
                if(len(cola)>0):
                    extrae=cola.popleft()
                else:
                    print('\nBusqueda terminada, NO se han encontrado caminos para el nodo destino')
                    cola.append(origen)
                    break
                if (extrae not in visitados):
                    visitados.append(extrae)
                    nodosRel=deque()
                    if(extrae.getNivel()<nivel):
                        for i in extrae.getAristas():
                            if(extrae.getNivel()==nivel-1 and len(i.getNodoDest().getAristasSN(extrae))>0):
                                terminar=0

                            if(i.getNodoDest() not in visitados  and i.getNodoDest() not in cola):
                                i.getNodoDest().setNivel(extrae.getNivel()+1)
                                nodosRel.append(i.getNodoDest())
                        nodosRel = deque(ordenarHijos(nodosRel))
                        cola=nodosRel+cola

                    print('---------------------')
                    print('Extrae:\t\t' + extrae.getNombre())
                    print('Cola:\t\t' + ' '.join(x.getNombre() for x in cola))
                    print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))
                    aux = aux + 1
            nivel += 1
        toc = time.perf_counter()
        print(Fore.CYAN + "\nTiempo transcurrido " + str((toc-tic)*1000)+ 'ms')
        #print(Fore.CYAN+ f"\nTiempo transcurrido {toc - tic:0.8f} segundos")

    def Bidireccional(self, origen, destino):
        # Inicializar variables
        colaP = deque()  # cola regresiva
        colaR = deque()  # cola progresiva

        visitadosP = []
        visitadosR = []
        aux = 0
        tic = time.perf_counter()
        if (origen == destino):
            print("¡Nodo encontrado")
        else:
            colaP.append(origen)
            # visitadosP.append(origen)
            colaR.append(destino)
            # visitadosR.append(destino)

            while len(colaP) > 0 and len(colaR) > 0 and aux == 0:
                extraeP = colaP.popleft()
                if extraeP not in visitadosP:
                    visitadosP.append(extraeP)
                    nodosRel = []
                    for i in extraeP.getAristas():
                        if i.getNodoDest() not in visitadosP and i.getNodoDest() not in colaP:
                            nodosRel.append(i.getNodoDest())
                    colaP += nodosRel

                    print('----------Progresivo-----------')
                    print('Extrae:\t\t' + extraeP.getNombre())
                    print('Cola:\t\t' + ' '.join(x.getNombre() for x in colaP))
                print('visitados:\t' + ' '.join(x.getNombre() for x in visitadosP))


                extraeR = colaR.popleft()
                if extraeR not in visitadosR:
                    visitadosR.append(extraeR)
                    nodosRel = []
                    for i in extraeR.getAristas():
                        if i.getNodoDest() not in visitadosR:
                            nodosRel.append(i.getNodoDest())
                    nodosRel = ordenarHijos(nodosRel)
                    colaR += nodosRel

                    print('----------Regresivo-----------')
                    print('Extrae:\t\t' + extraeR.getNombre())
                    print('Cola:\t\t' + ' '.join(x.getNombre() for x in colaR))
                print('visitados:\t' + ' '.join(x.getNombre() for x in visitadosR))

                if (extraeP == extraeR): #if (extraeP in visitadosR):
                    print('Caminos encontrados en nodo ' + extraeP.getNombre())
                    aux = 1
                    break
                else:
                    for i in visitadosP:
                        if i in visitadosR:
                            print('Caminos encontrados en nodo ' + i.getNombre())
                            aux = 1
                            break
                print('\n')
        toc = time.perf_counter()
        print(Fore.CYAN + "\nTiempo transcurrido " + str((toc-tic)*1000)+ 'ms')
        #print(Fore.CYAN + f"\nTiempo transcurrido {toc - tic:0.8f} segundos")

    def costoUniforme(self,origen,destinos):
        """tic = time.perf_counter()
        cola = deque()
        nodo = Nodo('')
        cola.append([0, nodo, origen])
        extrae = [0, nodo, nodo]
        visitados = deque()

        while (len(cola)>0 and extrae[1] not in destinos):
            extrae=cola.popleft()
            for i in extrae[2].getAristasSN(extrae[2]):
                if (i.getPeso() != ''):
                    valAcum = int(i.getPeso()) + int(extrae[0])
                    arr = [valAcum, extrae[2], i.getNodoDest()]
                    p = 0
                    o = 0
                    for j in visitados:
                        if extrae[2] == j[1] and i.getNodoDest() == j[2] and valAcum >= j[0]:
                            p = 1
                    for k in cola:
                        if extrae[2] == k[1] and i.getNodoDest() == k[2] and valAcum >= k[0]:
                            o = 1
                    if p != 1 and o != 1:
                        cola.append(arr)
            cola = deque(sorted(list(cola), key=itemgetter(0)))

            print('----------------------------------------')
            print('Extrae:\t\t' + extrae[1].getNombre()+''+str(extrae[0]))
            print('Cola:\t\t' + ' '.join(x[1].getNombre()+''+str(x[0]) for x in cola))

            if(extrae[1] in destinos):
                print('\n¡Nodo Encontrado!')
                break
            if(len(cola)==0):
                break;
        toc = time.perf_counter()
        print(Fore.CYAN + "\nBusqueda terminada en " + str((toc-tic)*1000)+ 'ms')"""
        tic = time.perf_counter()
        cola = deque()
        nodo = Nodo('')
        cola.append([0, nodo, origen])
        extrae = [0, nodo, nodo]
        visitados = deque()

        while (len(cola) > 0 and extrae[2] not in destinos):

            extrae = cola.popleft()
            visitados.append(extrae)
            if (extrae[1] in destinos):
                print('\n¡Nodo Encontrado!')
                break
            for i in extrae[2].getAristasSN(extrae[2]):
                if (i.getPeso() != ''):
                    valAcum = int(i.getPeso()) + int(extrae[0])
                    arr = [valAcum, extrae[2], i.getNodoDest()]
                    p = 0
                    o = 0
                    for j in visitados:
                        if extrae[2] == j[1] and i.getNodoDest() == j[2] and valAcum >= j[0]:
                            p = 1
                    for k in cola:
                        if extrae[2] == k[1] and i.getNodoDest() == k[2] and valAcum >= k[0]:
                            o = 1
                    if p != 1 and o != 1:
                        cola.append(arr)

            cola = deque(sorted(list(cola), key=itemgetter(0)))

            print('extrae:\t\t\t' + str(extrae[0]) + '' + extrae[1].getNombre() + '' + extrae[2].getNombre())
            print('Cola:\t\t' + ''.join(' ' + str(+x[0]) + '' + x[1].getNombre() + '' + x[2].getNombre() for x in cola))
            print('visitados:\t' + ''.join(
                ' ' + str(+x[0]) + '' + x[1].getNombre() + '' + x[2].getNombre() for x in visitados))
            print('-----------------------------')
            #if (cola):
             #   print('extrae:\t\t\t' + str(cola[0][0]) + '' + cola[0][1].getNombre() + '' + cola[0][2].getNombre())
            if (len(cola) == 0):
                break;

        toc = time.perf_counter()
        print(Fore.CYAN + "\nBusqueda terminada en " + str((toc - tic) * 1000) + 'ms')

    def costoUniformeSF(self,origen):
        tic = time.perf_counter()
        cola=deque()
        nodo = Nodo('')
        cola.append([0,nodo,origen])
        extrae=[0,nodo,nodo]
        visitados=deque()

        while (len(cola)>0 ):
            extrae=cola.popleft()
            visitados.append(extrae)

            for i in extrae[2].getAristasSN(extrae[2]):
                if (i.getPeso()!=''):
                    valAcum=int(i.getPeso())+int(extrae[0])
                    arr=[valAcum,extrae[2],i.getNodoDest()]
                    p=0
                    o=0
                    for j in visitados:
                        if extrae[2]==j[1] and i.getNodoDest()==j[2] and valAcum>=j[0]:
                            p=1
                    for k in cola:
                        if extrae[2]==k[1] and i.getNodoDest()==k[2] and valAcum>=k[0]:
                            o=1
                    if p!=1 and o!=1:
                        cola.append(arr)

            cola = deque(sorted(list(cola), key=itemgetter(0)))

            print('Cola:\t\t' + ''.join(' ' + str(+x[0]) + '' + x[1].getNombre() + '' + x[2].getNombre() for x in cola))
            print('visitados:\t\t' + ''.join(
                ' ' + str(+x[0]) + '' + x[1].getNombre() + '' + x[2].getNombre() for x in visitados))
            print('-----------------------------')
            if (cola):
                print('extrae:\t\t' + str(cola[0][0]) + '' + cola[0][1].getNombre() + '' + cola[0][2].getNombre())


        toc = time.perf_counter()
        print(Fore.CYAN + "\nBusqueda terminada en " + str((toc-tic)*1000)+ 'ms')
