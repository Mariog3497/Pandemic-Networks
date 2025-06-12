import unittest
from unittest.mock import MagicMock, patch
import networkx as nx


from pandemic import Pandemic

class TestPandemic(unittest.TestCase):
    def setUp(self):
        self.mock_network = MagicMock()
        self.mock_network.graph.return_value = nx.path_graph(5)
        self.pandemic = Pandemic(self.mock_network)

    def test_initialize_state(self):
        self.pandemic.initializeState()
        states = self.pandemic.state
        self.assertEqual(len(states), 5)
        infected = [node for node, state in states.items() if state == 'I']
        susceptible = [node for node, state in states.items() if state == 'S']
        self.assertEqual(len(infected), 1) 
        self.assertEqual(len(susceptible), 4)

    def test_update_history(self):
        self.pandemic.state = {0:'S', 1:'S', 2:'I', 3:'I', 4:'R'}
        self.pandemic.history = {'S':[], 'I':[], 'R':[], 'D':[]}
        self.pandemic.updateHistory()
        self.assertEqual(self.pandemic.history['S'][-1], 2)
        self.assertEqual(self.pandemic.history['I'][-1], 2)
        self.assertEqual(self.pandemic.history['R'][-1], 1)
        self.assertEqual(self.pandemic.history['D'][-1], 0)

    @patch('random.random')
    def test_pandemic_step_infection_and_recovery(self, mock_random):
        self.pandemic.state = {0:'I', 1:'S', 2:'S'}
        self.pandemic.graph = nx.path_graph(3)

        mock_random.side_effect = [0.5, 0.2]

        self.pandemic.infection = 0.7
        self.pandemic.recovery = 0.3
        self.pandemic.pandemicStep()

        self.assertEqual(self.pandemic.state[1], 'I')
        self.assertEqual(self.pandemic.state[0], 'R')

    @patch('matplotlib.pyplot.show')
    def test_generate_pandemic_evolution_calls(self, mock_show):
        with patch.object(self.pandemic, 'initializeState') as mock_init, \
             patch.object(self.pandemic, 'updateHistory') as mock_update, \
             patch.object(self.pandemic, 'simulate') as mock_simulate:

            self.pandemic.generate_pandemic_evolution()
            mock_init.assert_called_once()
            mock_update.assert_called_once()
            mock_simulate.assert_called_once()

if __name__ == '__main__':
    unittest.main()