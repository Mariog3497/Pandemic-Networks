from abc import ABC, abstractmethod
from util import chooseOption
import networkx as nx

class Network(ABC):
    def __init__(self,simulated, name):
        self.nodes = None
        self.simulated = simulated
        self.name = name
    
    @abstractmethod
    def configuration(self):
        pass
    
    @abstractmethod
    def graph(self):
        pass
    
        
class ErdosRenyi(Network):
    def __init__(self,simulated):
        super().__init__(simulated, "Erdős-Rényi")
        self.nodes = 10
        self.probabilityConnections = 0.3
        

    def configuration(self):
        

        if(not self.simulated):
            print("Set number of nodes (N)")
            self.nodes = chooseOption(1, 100, False)
            
            print("Set probability of two nodes connection (P)")
            self.probabilityConnections = chooseOption(0, 1, True)
            
            self.simulated = False

    def graph(self):
        return nx.erdos_renyi_graph(self.nodes,self.probabilityConnections)
        
    
    def __str__(self):
        return (
            f"Network Erdős-Rényi: "
            f"Number of nodes set (N): {self.nodes} "
            f"Probability of edge (P): {self.probabilityConnections}"
    )


class WattsStrogatz(Network):
    def __init__(self,simulated):
        super().__init__(simulated, "Watts-Strogatz")
        self.nodes = 10
        self.initialDirectNeighbours = 4
        self.probabilityRewired = 0.3

    def configuration(self):
        if(not self.simulated):
            print("Set number of nodes (N)")
            self.nodes = chooseOption(1, 100, False)
            self.initialDirectNeighbours = -1
            print("Number of nearest neighbors each node is initially connected to (K)")
            while self.initialDirectNeighbours < 0 or self.initialDirectNeighbours >= self.nodes or self.initialDirectNeighbours % 2 != 0:
                self.initialDirectNeighbours = chooseOption(0,self.nodes,False)
                if self.initialDirectNeighbours < 0 or self.initialDirectNeighbours >= self.nodes or self.initialDirectNeighbours % 2 != 0:
                    print(f"\033[91m❌ k must be greater or equal 0, smaller than nodes and even '{self.initialDirectNeighbours}' is not a valid option\033[0m")
                
            print("Set rewire probability (P)")
            self.probabilityRewired = chooseOption(0, 1, True)
            
            self.simulated = False
            
    def graph(self):
        return nx.watts_strogatz_graph(self.nodes, self.initialDirectNeighbours, self.probabilityRewired)
    
    def __str__(self):
        return (
            f"Network Watts-Strogatz: "
            f"Nodes (N): {self.nodes} "
            f"Neighbors (K): {self.initialDirectNeighbours} "
            f"Rewire prob (P): {self.probabilityRewired}"
        )

class BarabasiAlbert(Network):
    def __init__(self,simulated):
        super().__init__(simulated, "Barabasi Albert")
        self.nodes = 10
        self.numberOfEdges = 2

    def configuration(self):
        if(not self.simulated):
            print("Set number of nodes (N)")
            self.nodes = chooseOption(1, 100, False)
            print("Number of edges to attach from each new node (M)")
            self.numberOfEdges = chooseOption(1,self.nodes,False)
            self.simulated = False
    
    def graph(self):
        return nx.barabasi_albert_graph(self.nodes, self.numberOfEdges)
    
    
    def __str__(self):
        return (
            f"Network Barabasi Albert: "
            f"Nodes (N): {self.nodes} "
            f"Edges per node (M): {self.numberOfEdges}"
        )
  