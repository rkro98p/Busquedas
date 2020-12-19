def a_estrella(grafo,nodoInicial,nodoFinal):
        cola=deque()
        cola.append([0,"",nodoInicial])
        actual=[0,"",""]
        aux=0
        while cola:
            actual=cola.popleft()
            for i in grafo.getVertice(actual[2]).getConexion():
                cola.append([int(i.getCostoV(i))+int(grafo.getVertice(actual[2]).getPeso(i)),grafo.getVertice(actual[2]).getId(),i.getId()])
                if i.getId() == nodoFinal:
                    aux=1
            cola = deque(sorted(list(cola), key=itemgetter(0)))
            print(cola)
            print('Camino:' +str(actual[0])+''+str(actual[1])+''+str(actual[2]))
            if(aux==1):
                print('¡Nodo encontrado!')
                break



a_estrella(g,"S","E")