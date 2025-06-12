from menu import *
from pandemic import Pandemic
from colorama import init, Fore
from network import ErdosRenyi, WattsStrogatz, BarabasiAlbert

class SimulationApp:
    def __init__(self, menu):
        self.menu = menu
        self.network = None
        self.pandemic = None

    def run(self):
        option = None
        while option != Menu.OPTION_6_EXIT:
            self.menu.clean() 
            option = self.menu.main() 
            self.handle_option(option) 

    def handle_option(self, option):
        if option == Menu.OPTION_1_NETWORK_SETTINGS:
            self.configure_network()
        elif option == Menu.OPTION_2_SHOW_NETWORK_SETTINGS:
            self.show_network_configuration()
        elif option == Menu.OPTION_3_PANDEMIC_SETTINGS:
            self.configure_pandemic()
        elif option == Menu.OPTION_4_SHOW_PANDEMIC_SETTINGS:
            self.show_pandemic_configuration()
        elif option == Menu.OPTION_5_GENERATE_PANDEMIC_SIMULATION:
            self.generate_simulation()

    def configure_network(self):
        self.network = self.get_network()

    def show_network_configuration(self):
        if self.network:
            self.menu.clean()
            self.menu.menu_show_configuration_network(self.network)
        else:
            self.menu.error_message("You must first configure your network")
        self.menu.press_to_continue()

    def configure_pandemic(self):
        if self.network:
            self.menu.clean()
            self.pandemic = self.menu.pandemic(self.network)
        else:
            self.menu.error_message("You must first configure your network")
            self.menu.press_to_continue()

    def show_pandemic_configuration(self):
        if self.pandemic:
            self.menu.clean()
            self.menu.menu_show_configuration_pandemic(self.pandemic)
        else:
            self.menu.error_message("You must first configure your pandemic")
        self.menu.press_to_continue()

    def generate_simulation(self):
        if self.pandemic:
            self.pandemic.generate_pandemic_evolution()
        else:
            self.menu.error_message("You must first configure your pandemic")
            self.menu.press_to_continue()

    def get_network(self):
        self.menu.clean()
        type_network = self.menu.menu_choose_networks()
        self.menu.clean()
        simulated = self.menu.menu_defualt_configured_network()

        network = None
        if type_network == 1:
            network = ErdosRenyi(simulated)
        elif type_network == 2:
            network = WattsStrogatz(simulated)
        elif type_network == 3:
            network = BarabasiAlbert(simulated)
        else:
            self.menu.error_message("Invalid network type selected")
            return None

        network = self.menu.menu_set_configuration_network(network)
        return network


def main():
    init()
    menu = Menu()
    app = SimulationApp(menu)
    app.run()


if __name__ == "__main__":
    main()
