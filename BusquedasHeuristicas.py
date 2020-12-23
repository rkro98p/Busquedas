from collections import deque
from operator import itemgetter
from colorama import Fore
from colorama import init
init(autoreset=True)
import time

def ordenarHijos(hijos):
    hijos = sorted(hijos, key=lambda x: x.getNombre())
    return hijos

from Nodo import Nodo


class BusquedaH():
    def AscensoColina(self,origen,destinos):
        tic = time.perf_counter()
        actual=origen
        while (True):
            print('actual:\t'+actual.getNombre()+'\t('+actual.getNombre()+')='+actual.getValor())
            if(actual in destinos):
                print('¡Nodo encontrado!')
                break
            if(len(actual.getAristas())>0 or actual.getValor()==0):
                aux=0
                i=0
                for i in actual.getAristas():
                    if int(i.getNodoDest().getValor())<=int(actual.getValor()):
                        actual=i.getNodoDest()
                        aux=1
                if(aux==0):
                    print('No se puede mejorar')
                    break

            else:
                print(actual.getNombre()+' '+actual.getValor()+'No se puede mejorar')
                break
        toc = time.perf_counter()
        print(Fore.CYAN + "\nTiempo transcurrido " + str((toc-tic)*1000) + 'ms')
        ##print(f"\nTiempo transcurrido {toc - tic:0.8f} segundos")

    def PrimeroMejor(self,origen,destinos):
        tic = time.perf_counter()
        cola=deque()
        cola.append(origen)
        visitados=deque()
        ban=0
        print('cola:\t'+origen.getNombre())
        while(len(cola)>0):
            actual=cola.popleft()
            print('-----------------------------')
            print('extrae:\t'+actual.getNombre())
            visitados.append(actual)
            if (actual in destinos):
                print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))
                print('¡Nodo encontrado!')
                break
            if(len(actual.getAristas())>0):
                hijos=list()
                for i in actual.getAristas():
                    if (i.getNodoDest() not in visitados and i.getNodoDest() not in cola):
                        hijos.append(i.getNodoDest())
                    ##if i.getNodoDest() in destinos:
                        #ban=1
                      ##  break
                hijos = sorted(hijos, key=lambda x: int(x.valor))
                #print(''.join(x.getNombre() + '' + x.valor+ " " for x in hijos))

                cola=deque(hijos)+cola
            print('cola:\t' + ' '.join(x.getNombre() for x in cola))
            print('visitados:\t' + ' '.join(x.getNombre() for x in visitados))
            #if(ban==1):
             #   print('¡Nodo encontrado!')

              #  break
        toc = time.perf_counter()
        print(Fore.CYAN + "\nTiempo transcurrido " + str((toc-tic)*1000)+ 'ms')
        #print(f"\nTiempo transcurrido {toc - tic:0.8f} segundos")
    def Aestrella(self, origen, destinos):
        tic = time.perf_counter()
        cola = deque()
        nodo = Nodo('')
        cola.append([0, nodo, origen])
        actual = [0, nodo, nodo]
        visitados=deque()

        aux = 0

        while len(cola)>0:
            actual=cola.popleft()
            visitados.append(actual)
            for i in actual[2].getAristas():
                pesoAcumulado=int(i.getPeso())+int(i.getNodoDest().getValor())
                arr=[pesoAcumulado,actual[2],i.getNodoDest()]
                if actual[2]==origen:
                    cola.append(arr)
                else:
                    p=0 #bandera para controlar nodos repetidos
                    for j in deque(visitados):
                        #print(actual[2].getNombre()+'=='+j[1].getNombre()+' y '+i.getNodoDest().getNombre()+'=='+j[2].getNombre()+' '+str(pesoAcumulado)+'-'+str(j[0]))
                        if actual[2]==j[1] and i.getNodoDest()==j[2] and pesoAcumulado>=j[0]:
                            p=1
                    if p!=1:
                        cola.append(arr)
                if i.getNodoDest() in destinos:
                    aux = 1
            cola = deque(sorted(list(cola), key=itemgetter(0)))
            print('Cola:\t\t' + ''.join(' '+str(+x[0])+''+x[1].getNombre() + '' + x[2].getNombre() for x in cola))
            print('visitados:\t\t' + ''.join(' ' + str(+x[0]) + '' + x[1].getNombre() + '' + x[2].getNombre() for x in visitados))
            print('-----------------------------')
            if(cola):
                print('extrae:\t\t'+str(cola[0][0])+''+cola[0][1].getNombre() + '' + cola[0][2].getNombre())

            if (aux == 1):
                print('¡Nodo encontrado!')
                break
        toc = time.perf_counter()
        print(Fore.CYAN + "\nTiempo transcurrido " + str((toc-tic)*1000)+ 'ms')
        #print(f"\nTiempo transcurrido {toc - tic:0.8f} segundos")