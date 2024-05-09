import networkx as nx

from database.DAO import DAO
import networkx as n

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.areoporti = DAO.getAllAreoporti()
        self.voli = DAO.getAllVoli()
        self.rotte = DAO.getRotte()
        self.tratte = {}
        for a in self.areoporti:
            self.tratte[a.id] = a


    def buildGraph(self):
        self.grafo.add_nodes_from(self.areoporti)


    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def fillGraph(self, p_nodo, a_nodo): # aggiungo gli archi
        lista = []

        p = self.tratte[p_nodo]
        a = self.tratte[a_nodo]
        self.grafo.add_edge(p, a)
        distanza = self.getRotta(p_nodo, a_nodo)
        lista.append(f"Arco aggiunto tra {p.airport} e {a.airport} con la distanza media di {distanza}.")
        return lista

    def getRotta(self, p_nodo, a_nodo):
        for v in self.rotte:
            if v.origin_airport_id == p_nodo and v.destination_airport_id ==a_nodo:
                distanza_media = v.avg_distance
        return distanza_media




