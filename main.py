from menu import *
from pandemic import Pandemic
from colorama import init, Fore
from network import ErdosRenyi, WattsStrogatz, BarabasiAlbert

# Main application class to manage the simulation
class SimulationApp:
    
    def __init__(self, menu):
        # Initializes the application with a menu instance
        self.menu = menu
        self.network = None      # Stores the network configuration
        self.pandemic = None     # Stores the pandemic configuration

    # Main loop that keeps the application running until the user selects Exit
    def run(self):
        option = None
        while option != Menu.OPTION_6_EXIT:
            self.menu.clean()                  # Clear the screen/menu
            option = self.menu.main()         # Show main menu and get user input
            self.handle_option(option)        # Handle the selected option

    # Dispatches the selected menu option to the appropriate method
    def handle_option(self, option):
        if option == Menu.OPTION_1_NETWORK_SETTINGS:
            self.configure_network()                 # Option to configure a new network
        elif option == Menu.OPTION_2_SHOW_NETWORK_SETTINGS:
            self.show_network_configuration()        # Option to display the current network configuration
        elif option == Menu.OPTION_3_PANDEMIC_SETTINGS:
            self.configure_pandemic()                # Option to configure pandemic parameters
        elif option == Menu.OPTION_4_SHOW_PANDEMIC_SETTINGS:
            self.show_pandemic_configuration()       # Option to display current pandemic settings
        elif option == Menu.OPTION_5_GENERATE_PANDEMIC_SIMULATION:
            self.generate_simulation()               # Option to run the pandemic simulation

    # Prompts the user to configure and create a network
    def configure_network(self):
        self.network = self.get_network()

    # Displays the current network configuration
    def show_network_configuration(self):
        if self.network:
            self.menu.clean()
            self.menu.menu_show_configuration_network(self.network)
        else:
            self.menu.error_message("You must first configure your network")
        self.menu.press_to_continue()

    # Prompts the user to configure a pandemic, but only if a network exists
    def configure_pandemic(self):
        if self.network:
            self.menu.clean()
            self.pandemic = self.menu.pandemic(self.network)
        else:
            self.menu.error_message("You must first configure your network")
            self.menu.press_to_continue()

    # Displays the current pandemic configuration
    def show_pandemic_configuration(self):
        if self.pandemic:
            self.menu.clean()
            self.menu.menu_show_configuration_pandemic(self.pandemic)
        else:
            self.menu.error_message("You must first configure your pandemic")
        self.menu.press_to_continue()

    # Executes the pandemic simulation based on the current configuration
    def generate_simulation(self):
        if self.pandemic:
            self.pandemic.generate_pandemic_evolution()
        else:
            self.menu.error_message("You must first configure your pandemic")
            self.menu.press_to_continue()

    # Interactively builds and returns a network object based on user input
    def get_network(self):
        self.menu.clean()
        type_network = self.menu.menu_choose_networks()              # User chooses network type
        self.menu.clean()
        simulated = self.menu.menu_defualt_configured_network()      # User chooses default or custom config

        network = None
        if type_network == 1:
            network = ErdosRenyi(simulated)                          # Create an Erdos-Renyi network
        elif type_network == 2:
            network = WattsStrogatz(simulated)                       # Create a Watts-Strogatz network
        elif type_network == 3:
            network = BarabasiAlbert(simulated)                      # Create a Barabási–Albert network
        else:
            self.menu.error_message("Invalid network type selected")
            return None

        # Apply user-defined configuration to the selected network
        network = self.menu.menu_set_configuration_network(network)
        return network


# Entry point of the program
def main():
    init()                      # Initialize colorama for colored terminal output
    menu = Menu()               # Create menu interface
    app = SimulationApp(menu)   # Create the simulation application
    app.run()                   # Start running the app


# Run main only if this file is executed directly
if __name__ == "__main__":
    main()
