from abc import ABC, abstractmethod
from menu import *
import networkx as nx
from menu import *

# Abstract base class representing a generic network
class Network(ABC):
    def __init__(self, simulated):
        # Number of nodes in the network (to be defined by subclass)
        self.nodes = None
        # Flag indicating if the network uses default simulation parameters
        self.simulated = simulated

    @abstractmethod
    def graph(self):
        # Method that must be implemented to return a NetworkX graph
        pass

# Erdős–Rényi random network model
class ErdosRenyi(Network):
    NAME = "Erdős-Rényi"

    def __init__(self, simulated):
        super().__init__(simulated)
        # Default number of nodes
        self.nodes = 10
        # Probability that an edge exists between any pair of nodes
        self.probabilityConnections = 0.3

    def graph(self):
        # Generate an Erdős-Rényi graph using NetworkX
        return nx.erdos_renyi_graph(self.nodes, self.probabilityConnections)

    def __str__(self):
        # String representation of the network configuration
        return (
            f"Network {ErdosRenyi.NAME}: "
            f"Number of nodes set (N): {self.nodes} "
            f"Probability of edge (P): {self.probabilityConnections}"
        )

# Watts–Strogatz small-world network model
class WattsStrogatz(Network):
    NAME = "Watts-Strogatz"

    def __init__(self, simulated):
        super().__init__(simulated)
        # Default number of nodes
        self.nodes = 10
        # Each node is connected to this number of nearest neighbors in ring topology
        self.initialDirectNeighbours = 4
        # Probability of rewiring each edge
        self.probabilityRewired = 0.3

    def graph(self):
        # Generate a Watts–Strogatz small-world graph using NetworkX
        return nx.watts_strogatz_graph(self.nodes, self.initialDirectNeighbours, self.probabilityRewired)

    def __str__(self):
        # String representation of the network configuration
        return (
            f"Network {WattsStrogatz.NAME}: "
            f"Nodes (N): {self.nodes} "
            f"Neighbors (K): {self.initialDirectNeighbours} "
            f"Rewire prob (P): {self.probabilityRewired}"
        )

# Barabási–Albert scale-free network model
class BarabasiAlbert(Network):
    NAME = "Barabasi Albert"

    def __init__(self, simulated):
        super().__init__(simulated)
        # Default number of nodes
        self.nodes = 10
        # Number of edges to attach from a new node to existing nodes
        self.numberOfEdges = 2

    def graph(self):
        # Generate a Barabási–Albert graph using NetworkX
        return nx.barabasi_albert_graph(self.nodes, self.numberOfEdges)

    def __str__(self):
        # String representation of the network configuration
        return (
            f"Network {BarabasiAlbert.NAME}: "
            f"Nodes (N): {self.nodes} "
            f"Edges per node (M): {self.numberOfEdges}"
        )
