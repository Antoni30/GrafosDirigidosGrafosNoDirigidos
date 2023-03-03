def recorrido(lista,cost):
    """
    Funcion que permite calcular el recorrido de una via

    Parametros
    ---------------------------------------------
    Lista de vias que recorre:lista
    Costo de cada via: cost

    Retorna
    --------------------------------------------
    Recorrido que realizo:costoT
    """
    #variablea para calcular el costo
    costoT=0
    #Recorre la lista de la via 
    for clave in lista:
        #busca el costo
        costoT+=cost[clave]
    #retorna el costo
    return costoT
if __name__=='__main__':
    #declaramos el grafo y los costos que tendra nuestro usuario
    graph, cost = [[] for i in range(3)], {}
    #declaramos el nombre los nodos  que ocupara nuestro grafo 
    casa=0
    casaVecinaLaura=1
    casaVecinaMarta=2
    tienda=3
    #Ingresamos los grafos a nuestro nodo
    graph[casa].append(casa)
    graph[casa].append(casaVecinaLaura)
    graph[casa].append(casaVecinaMarta)
    graph[casaVecinaLaura].append(tienda)
    graph[casaVecinaMarta].append(casaVecinaLaura)
   
    #Ingresamos los costos y sus direcciones
    cost[(casa,casa)]=0
    cost[(casa,casaVecinaLaura)]=2
    cost[(casaVecinaLaura,casa)]=2
    cost[(casaVecinaLaura,tienda)]=6
    cost[(tienda,casaVecinaLaura)]=6
    cost[(casa,casaVecinaMarta)]=5
    cost[(casaVecinaMarta,casa)]=5
    cost[(casaVecinaMarta,casaVecinaLaura)]=4
    cost[(casaVecinaLaura,casaVecinaMarta)]=4

    listaRecorrer1=[(0,0),(0,1),(1,3),(1,0),(3,1)]
    listaRecorrer2=[(0,0),(0,2),(2,1),(1,3),(2,0),(1,2),(3,1)]
    
    print("Recorrido de la primera Via es {}".format(recorrido(listaRecorrer1,cost)))
    print("Recorrido de la segunda Via es {}".format(recorrido(listaRecorrer2,cost)))


