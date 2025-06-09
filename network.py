from abc import ABC, abstractmethod
from menu import *
import networkx as nx
from menu import *

class Network(ABC):
    def __init__(self,simulated):
        self.nodes = None
        self.simulated = simulated
       
    @abstractmethod
    def graph(self):
        pass
       
class ErdosRenyi(Network):
    NAME = "Erdős-Rényi" 
    def __init__(self,simulated):
        super().__init__(simulated)
        self.nodes = 10
        self.probabilityConnections = 0.3
        
    def graph(self):
        return nx.erdos_renyi_graph(self.nodes,self.probabilityConnections)
        
    
    def __str__(self):
        return (
            f"Network {ErdosRenyi.NAME}: "
            f"Number of nodes set (N): {self.nodes} "
            f"Probability of edge (P): {self.probabilityConnections}"
    )


class WattsStrogatz(Network):
    NAME = "Watts-Strogatz" 
    def __init__(self,simulated):
        super().__init__(simulated)
        self.nodes = 10
        self.initialDirectNeighbours = 4
        self.probabilityRewired = 0.3
                    
    def graph(self):
        return nx.watts_strogatz_graph(self.nodes, self.initialDirectNeighbours, self.probabilityRewired)
    
    def __str__(self):
        return (
            f"Network {WattsStrogatz.NAME}: "
            f"Nodes (N): {self.nodes} "
            f"Neighbors (K): {self.initialDirectNeighbours} "
            f"Rewire prob (P): {self.probabilityRewired}"
        )

class BarabasiAlbert(Network):
    NAME = "Barabasi Albert"
    def __init__(self,simulated):
        super().__init__(simulated)
        self.nodes = 10
        self.numberOfEdges = 2
            
    def graph(self):
        return nx.barabasi_albert_graph(self.nodes, self.numberOfEdges)
    
    
    def __str__(self):
        return (
            f"Network {BarabasiAlbert.NAME}: "
            f"Nodes (N): {self.nodes} "
            f"Edges per node (M): {self.numberOfEdges}"
        )
    