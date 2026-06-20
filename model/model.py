import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMapCircuits = {}
        self._grafo = nx.Graph()

    def getAllYears(self):
        return DAO.getAllYears()

    def creaGrafo(self, year1, year2):

        self._grafo.clear()
        circuits = DAO.getAllCircuits()


        for circuit in circuits:
            for key in DAO.getYearofCircuit(circuit.circuitId, year1, year2):
                circuit.results[key] = []
                for k, value in DAO.getDetails(circuit.circuitId, year1, year2):
                    if k == key:
                        circuit.results[key].append(value)


        for circuit in circuits:
            self._idMapCircuits[circuit.circuitId] = circuit

        self._grafo.add_nodes_from(circuits)

        for u in self._grafo.nodes():
            for v in self._grafo.nodes():
                if u.circuitId < v.circuitId:
                    if len(u.results) > 0 and len(v.results) > 0:
                        peso = int(DAO.getPeso(u.circuitId, year1, year2)[0]) + int(DAO.getPeso(v.circuitId, year1, year2)[0])
                        self._grafo.add_edge(u, v, weight=peso)


        print(len(self._grafo.nodes))
        print(len(self._grafo.edges))

    def getDettagliGrafo(self):
        return len(self._grafo.nodes) , len(self._grafo.edges)

    def getCompConn(self):
        largest_cc = list(max(nx.connected_components(self._grafo), key=len))

        res = []
        for c in largest_cc:
            res.append((c, self._getMaxEdge(c)))

        res.sort(key=lambda x: x[1], reverse=True)

        return res

    def _getMaxEdge(self, c):

        counter = 0
        for i in self._grafo.neighbors(c):
            if counter < self._grafo[c][i]["weight"]:
                counter = self._grafo[c][i]["weight"]

        return counter