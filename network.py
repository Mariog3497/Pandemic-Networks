from abc import ABC, abstractmethod
from util import chooseOption

class Network(ABC):
    def __init__(self,simulated):
        self.nodes = None
        self.simulated = simulated
    
    @abstractmethod
    def configuration(self):
        pass
    
        
class ErdosRenyi(Network):
    def __init__(self,simulated):
        super().__init__(simulated)
        self.nodes = 10
        self.probabilityConnections = 0.3

    def configuration(self):
        
        
        if(not self.simulated):
            print("Set number of nodes (N)")
            self.nodes = chooseOption(1, 100, False)
            
            print("Set probability of two nodes connection (P)")
            self.probabilityConnections = chooseOption(0, 1, True)
            
            self.simulated = False

    def __str__(self):
        return (f"Network Erdős-Rényi configured:\n"
                f"\tNumber of nodes set (N): {self.nodes}\n"
                f"\tProbability that an edge exists between two nodes (P): {self.probabilityConnections}")


class WattsStrogatz(Network):
    def __init__(self,simulated):
        super().__init__(simulated)
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
    
    def __str__(self):
        return (
            "Network Watts-Strogatz configured:\n"
            f"\tNumber of nodes set (N): {self.nodes}\n"
            f"\tNumber of nearest neighbors each node is initially connected to (K): {self.initialDirectNeighbours}\n"
            f"\tRewire Probability set (P): {self.probabilityRewired}"
            )

class BarabasiAlbert(Network):
    def __init__(self,simulated):
        super().__init__(simulated)
        self.nodes = 10
        self.numberOfEdges = 2

    def configuration(self):
        if(not self.simulated):
            print("Set number of nodes (N)")
            self.nodes = chooseOption(1, 100, False)
            print("Number of edges to attach from each new node (M)")
            self.numberOfEdges = chooseOption(1,self.nodes,False)
            self.simulated = False
    
    def __str__(self):
        return (
            "Network Barabasi configured:\n"
            f"\tNumber of nodes set (N): {self.nodes}\n"
            f"\tNumber of edges to attach from each new node (M): {self.numberOfEdges}"
        )   