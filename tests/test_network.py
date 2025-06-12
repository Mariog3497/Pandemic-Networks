import unittest
import networkx as nx
from network import ErdosRenyi, WattsStrogatz, BarabasiAlbert, Network


class TestNetworkSubclasses(unittest.TestCase):

    def test_erdos_renyi_graph_generation(self):
        net = ErdosRenyi(simulated={})
        g = net.graph()
        self.assertIsInstance(g, nx.Graph)
        self.assertEqual(len(g.nodes), net.nodes)
        self.assertTrue(0 <= net.probabilityConnections <= 1)

    def test_erdos_renyi_str(self):
        net = ErdosRenyi(simulated={})
        s = str(net)
        self.assertIn("Erdős-Rényi", s)
        self.assertIn("Number of nodes set", s)
        self.assertIn(str(net.nodes), s)
        self.assertIn(str(net.probabilityConnections), s)

    def test_watts_strogatz_graph_generation(self):
        net = WattsStrogatz(simulated={})
        g = net.graph()
        self.assertIsInstance(g, nx.Graph)
        self.assertEqual(len(g.nodes), net.nodes)
        self.assertTrue(0 <= net.probabilityRewired <= 1)

    def test_watts_strogatz_str(self):
        net = WattsStrogatz(simulated={})
        s = str(net)
        self.assertIn("Watts-Strogatz", s)
        self.assertIn(str(net.initialDirectNeighbours), s)
        self.assertIn(str(net.probabilityRewired), s)

    def test_barabasi_albert_graph_generation(self):
        net = BarabasiAlbert(simulated={})
        g = net.graph()
        self.assertIsInstance(g, nx.Graph)
        self.assertEqual(len(g.nodes), net.nodes)

    def test_barabasi_albert_str(self):
        net = BarabasiAlbert(simulated={})
        s = str(net)
        self.assertIn("Barabasi Albert", s)
        self.assertIn(str(net.nodes), s)
        self.assertIn(str(net.numberOfEdges), s)

    def test_abstract_network_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Network(simulated={})

if __name__ == '__main__':
    unittest.main()
