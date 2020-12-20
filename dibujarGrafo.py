import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Dibujar():
    def __init__(self):
        self.g = nx.DiGraph()
    def addNode(self,nombre, peso):
        self.g.add_node(nombre,h=peso)
    def addEdge(self,a,b,valor):
        self.g.add_edge(a,b,weigth=valor)
    def dibujar(self):
        #nx.draw(self.g, with_labels=True)
        h = nx.get_node_attributes(self.g, 'h')
        #nx.draw(self.g, h)
        labels = nx.get_edge_attributes(self.g,'weight')
        nx.draw_networkx_edge_labels(self.g, h, edge_labels=labels)
        nx.draw_shell(self.g,with_labels=True, node_size=1500, edge_cmap=plt.cm.Reds)
        #nx.draw_networkx_edge_labels(self.g, edge_labels=labels)
        plt.draw()
        plt.show()

"""g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edge(1, 2)
g.add_edge(4, 2)
g.add_edge(3, 5)
g.add_edge(2, 3)
g.add_edge(5, 4)"""


