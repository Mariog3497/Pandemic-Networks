import unittest
from unittest.mock import MagicMock, patch
from main import SimulationApp
from menu import Menu
from pandemic import Pandemic
from network import ErdosRenyi, WattsStrogatz, BarabasiAlbert


class TestSimulationApp(unittest.TestCase):

    def setUp(self):
        self.mock_menu = MagicMock(spec=Menu)
        self.app = SimulationApp(self.mock_menu)

    def test_init(self):
        self.assertEqual(self.app.menu, self.mock_menu)
        self.assertIsNone(self.app.network)
        self.assertIsNone(self.app.pandemic)

    def test_configure_network_sets_network(self):
        mock_network = MagicMock(spec=ErdosRenyi)
        self.app.get_network = MagicMock(return_value=mock_network)
        self.app.configure_network()
        self.assertEqual(self.app.network, mock_network)

    def test_show_network_configuration_when_configured(self):
        self.app.network = MagicMock()
        self.app.show_network_configuration()
        self.mock_menu.menu_show_configuration_network.assert_called_once_with(self.app.network)

    def test_show_network_configuration_when_not_configured(self):
        self.app.network = None
        self.app.show_network_configuration()
        self.mock_menu.error_message.assert_called_once_with("You must first configure your network")
        self.mock_menu.press_to_continue.assert_called_once()

    def test_configure_pandemic_when_network_exists(self):
        self.app.network = MagicMock()
        pandemic_mock = MagicMock(spec=Pandemic)
        self.mock_menu.pandemic.return_value = pandemic_mock
        self.app.configure_pandemic()
        self.assertEqual(self.app.pandemic, pandemic_mock)

    def test_configure_pandemic_when_network_missing(self):
        self.app.network = None
        self.app.configure_pandemic()
        self.mock_menu.error_message.assert_called_once_with("You must first configure your network")
        self.mock_menu.press_to_continue.assert_called_once()

    def test_show_pandemic_configuration_when_configured(self):
        self.app.pandemic = MagicMock()
        self.app.show_pandemic_configuration()
        self.mock_menu.menu_show_configuration_pandemic.assert_called_once_with(self.app.pandemic)

    def test_show_pandemic_configuration_when_not_configured(self):
        self.app.pandemic = None
        self.app.show_pandemic_configuration()
        self.mock_menu.error_message.assert_called_once_with("You must first configure your pandemic")
        self.mock_menu.press_to_continue.assert_called_once()

    def test_generate_simulation_when_pandemic_configured(self):
        self.app.pandemic = MagicMock()
        self.app.generate_simulation()
        self.app.pandemic.generate_pandemic_evolution.assert_called_once()

    def test_generate_simulation_when_pandemic_not_configured(self):
        self.app.pandemic = None
        self.app.generate_simulation()
        self.mock_menu.error_message.assert_called_once_with("You must first configure your pandemic")
        self.mock_menu.press_to_continue.assert_called_once()

    @patch('main.ErdosRenyi')
    def test_get_network_erdos_renyi(self, MockErdosRenyi):
        self.mock_menu.menu_choose_networks.return_value = 1
        self.mock_menu.menu_defualt_configured_network.return_value = {"nodes": 100, "p": 0.2}
        network_instance = MockErdosRenyi.return_value
        self.mock_menu.menu_set_configuration_network.return_value = network_instance

        result = self.app.get_network()
        self.assertEqual(result, network_instance)

    @patch('main.WattsStrogatz')
    def test_get_network_watts_strogatz(self, MockWattsStrogatz):
        self.mock_menu.menu_choose_networks.return_value = 2
        self.mock_menu.menu_defualt_configured_network.return_value = {"nodes": 100, "k": 4, "p": 0.1}
        network_instance = MockWattsStrogatz.return_value
        self.mock_menu.menu_set_configuration_network.return_value = network_instance

        result = self.app.get_network()
        self.assertEqual(result, network_instance)

    @patch('main.BarabasiAlbert')
    def test_get_network_barabasi_albert(self, MockBarabasiAlbert):
        self.mock_menu.menu_choose_networks.return_value = 3
        self.mock_menu.menu_defualt_configured_network.return_value = {"nodes": 100, "m": 2}
        network_instance = MockBarabasiAlbert.return_value
        self.mock_menu.menu_set_configuration_network.return_value = network_instance

        result = self.app.get_network()
        self.assertEqual(result, network_instance)

    def test_get_network_invalid_type(self):
        self.mock_menu.menu_choose_networks.return_value = 99
        result = self.app.get_network()
        self.assertIsNone(result)
        self.mock_menu.error_message.assert_called_once_with("Invalid network type selected")

    def test_handle_option_calls_correct_method(self):
        self.app.configure_network = MagicMock()
        self.app.show_network_configuration = MagicMock()
        self.app.configure_pandemic = MagicMock()
        self.app.show_pandemic_configuration = MagicMock()
        self.app.generate_simulation = MagicMock()

        self.app.handle_option(Menu.OPTION_1_NETWORK_SETTINGS)
        self.app.configure_network.assert_called_once()

        self.app.handle_option(Menu.OPTION_2_SHOW_NETWORK_SETTINGS)
        self.app.show_network_configuration.assert_called_once()

        self.app.handle_option(Menu.OPTION_3_PANDEMIC_SETTINGS)
        self.app.configure_pandemic.assert_called_once()

        self.app.handle_option(Menu.OPTION_4_SHOW_PANDEMIC_SETTINGS)
        self.app.show_pandemic_configuration.assert_called_once()

        self.app.handle_option(Menu.OPTION_5_GENERATE_PANDEMIC_SIMULATION)
        self.app.generate_simulation.assert_called_once()

    def test_run_loop_until_exit(self):
        self.mock_menu.main.side_effect = [
            Menu.OPTION_1_NETWORK_SETTINGS,
            Menu.OPTION_2_SHOW_NETWORK_SETTINGS,
            Menu.OPTION_6_EXIT,
        ]

        self.app.handle_option = MagicMock()
        self.app.run()

        self.assertEqual(self.app.handle_option.call_count, 3)
        self.app.handle_option.assert_any_call(Menu.OPTION_1_NETWORK_SETTINGS)
        self.app.handle_option.assert_any_call(Menu.OPTION_2_SHOW_NETWORK_SETTINGS)
        self.app.handle_option.assert_any_call(Menu.OPTION_6_EXIT)


if __name__ == '__main__':
    unittest.main()
