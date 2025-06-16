from network import *
from pandemic import *
from colorama import init, Fore
import re
import os

class Menu:
    
    OPTION_1_NETWORK_SETTINGS = 1  # Option to configure the network
    OPTION_2_SHOW_NETWORK_SETTINGS = 2  # Option to show the network configuration
    OPTION_3_PANDEMIC_SETTINGS = 3  # Option to configure the pandemic
    OPTION_4_SHOW_PANDEMIC_SETTINGS = 4  # Option to show the pandemic configuration
    OPTION_5_GENERATE_PANDEMIC_SIMULATION = 5  # Option to generate the pandemic simulation
    OPTION_6_EXIT = 6  # Option to exit the program
    
    def main(self):
        # Display the main simulator menu
        print(Fore.BLUE + "*----- [Network Simulator] ----------*" + Fore.RESET)
        print(Fore.BLUE + "|                                    |" + Fore.RESET)
        print(Fore.BLUE + "| 1. Network Settings                |" + Fore.RESET)
        print(Fore.BLUE + "| 2. Show Network configuration      |" + Fore.RESET)
        print(Fore.BLUE + "| 3. Pandemic Settings               |" + Fore.RESET)
        print(Fore.BLUE + "| 4. Show Pandemic configuration     |" + Fore.RESET)
        print(Fore.BLUE + "| 5. Generate pandemic evolution     |" + Fore.RESET)
        print(Fore.BLUE + "| 6. Exit                            |" + Fore.RESET)
        print(Fore.BLUE + "*------------------------------------*" + Fore.RESET)
        option = self.chooseOption(1, 6, False)
        return option

    def menu_choose_networks(self):
        # Display the network type selection menu
        print(Fore.BLUE + "*--------- [Choose Network] ---------*" + Fore.RESET)
        print(Fore.BLUE + "|                                    |" + Fore.RESET)
        print(Fore.BLUE + "| 1. Erdős-Rényi                     |" + Fore.RESET)
        print(Fore.BLUE + "| 2. Watts-Strogatz                  |" + Fore.RESET)
        print(Fore.BLUE + "| 3. Barabási-Albert                 |" + Fore.RESET)
        print(Fore.BLUE + "*------------------------------------*" + Fore.RESET)

        typeNetwork = self.chooseOption(1, 3, False)

        return typeNetwork
    
    def menu_defualt_configured_network(self):
        # Select between default or user-configured network
        print(Fore.BLUE + "*------- [Default or Configured Network] -------*" + Fore.RESET)
        print(Fore.BLUE + "|                                                |" + Fore.RESET)
        print(Fore.BLUE + "| 1. Default Network                             |" + Fore.RESET)
        print(Fore.BLUE + "| 2. Configured Network                          |" + Fore.RESET)
        print(Fore.BLUE + "*------------------------------------------------*" + Fore.RESET)

        optionSimulated = self.chooseOption(1, 2, False)
        simulated = (optionSimulated == 1)
        
        return simulated   

    def menu_show_configuration_network(self, network):
        # Display the current network configuration based on network type
        if ErdosRenyi.NAME == network.NAME:
            title_text = "[Erdos-Rényi Configuration]"
            width = 47  
            inner_width = width - 2  

            
            title_length = len(title_text)
            total_padding = inner_width - title_length
            left_padding = total_padding // 2
            right_padding = total_padding - left_padding
            title_line = "*" + "-" * left_padding + title_text + "-" * right_padding + "*"

            print(Fore.BLUE + title_line + Fore.RESET)
            print(Fore.BLUE + f"|{' ' * inner_width}|" + Fore.RESET)

            line1 = f"Number of nodes set (N): {network.nodes}"
            line2 = f"Probability of edge (P): {network.probabilityConnections}"

            print(Fore.BLUE + f"| {line1.ljust(inner_width - 1)}|" + Fore.RESET)
            print(Fore.BLUE + f"| {line2.ljust(inner_width - 1)}|" + Fore.RESET)
            print(Fore.BLUE + "*" + "-" * inner_width + "*" + Fore.RESET)

        elif WattsStrogatz.NAME == network.NAME:
            title_text = "[Watts–Strogatz Configuration]"
            width = 47
            inner_width = width - 2

            total_padding = inner_width - len(title_text)
            left_padding = total_padding // 2
            right_padding = total_padding - left_padding
            title_line = "*" + "-" * left_padding + title_text + "-" * right_padding + "*"

            print(Fore.BLUE + title_line + Fore.RESET)
            print(Fore.BLUE + f"|{' ' * inner_width}|" + Fore.RESET)

            info = str(network)
            nodes = re.search(r"Nodes \(N\): (\d+)", info)
            neighbors = re.search(r"Neighbors \(K\): (\d+)", info)
            rewire_prob = re.search(r"Rewire prob \(P\): ([0-9.]+)", info)

            if nodes and neighbors and rewire_prob:
                print(Fore.BLUE + f"| Nodes (N): {nodes.group(1):<33}|" + Fore.RESET)
                print(Fore.BLUE + f"| Neighbors (K): {neighbors.group(1):<29}|" + Fore.RESET)
                print(Fore.BLUE + f"| Rewire prob (P): {rewire_prob.group(1):<27}|" + Fore.RESET)
            else:
                print(Fore.BLUE + f"| {info.ljust(inner_width - 1)}|" + Fore.RESET)

            print(Fore.BLUE + "*" + "-" * inner_width + "*" + Fore.RESET)

        elif BarabasiAlbert.NAME == network.NAME:
            title_text = "[Barabási–Albert Configuration]"
            width = 47
            inner_width = width - 2

            total_padding = inner_width - len(title_text)
            left_padding = total_padding // 2
            right_padding = total_padding - left_padding
            title_line = "*" + "-" * left_padding + title_text + "-" * right_padding + "*"

            print(Fore.BLUE + title_line + Fore.RESET)
            print(Fore.BLUE + f"|{' ' * inner_width}|" + Fore.RESET)

            line1 = f"Nodes (N): {network.nodes}"
            line2 = f"Edges per node (M): {network.numberOfEdges}"

            print(Fore.BLUE + f"| {line1.ljust(inner_width - 1)}|" + Fore.RESET)
            print(Fore.BLUE + f"| {line2.ljust(inner_width - 1)}|" + Fore.RESET)
            print(Fore.BLUE + "*" + "-" * inner_width + "*" + Fore.RESET)

        else:
            print(Fore.BLUE + "Network configuration not recognized." + Fore.RESET)
    
    
    
    def menu_set_configuration_network(self, network):
        # Request the user to configure parameters based on network type
        if ErdosRenyi.NAME == network.NAME and not network.simulated:
            print("Set number of nodes (N)")
            network.nodes = self.chooseOption(1, 100, False)
            
            print("Set probability of two nodes connection (P)")
            network.probabilityConnections = self.chooseOption(0, 1, True)

        elif WattsStrogatz.NAME == network.NAME and not network.simulated:
            print("Set number of nodes (N)")
            network.nodes = self.chooseOption(1, 100, False)
            network.initialDirectNeighbours = -1
            print("Number of nearest neighbors each node is initially connected to (K)")
            while network.initialDirectNeighbours < 0 or network.initialDirectNeighbours >= network.nodes or network.initialDirectNeighbours % 2 != 0:
                network.initialDirectNeighbours = self.chooseOption(0,network.nodes,False)
                if network.initialDirectNeighbours < 0 or network.initialDirectNeighbours >= network.nodes or network.initialDirectNeighbours % 2 != 0:
                    print(f"\033[91m❌ k must be greater or equal 0, smaller than nodes and even '{network.initialDirectNeighbours}' is not a valid option\033[0m")
                
            print("Set rewire probability (P)")
            self.probabilityRewired = self.chooseOption(0, 1, True)
        elif BarabasiAlbert.NAME == network.NAME and not network.simulated:
            print("Set number of nodes (N)")
            network.nodes = self.chooseOption(1, 100, False)
            print("Number of edges to attach from each new node (M)")
            network.numberOfEdges = self.chooseOption(1,network.nodes,False)
        return network
    
    def pandemic(self, network):
        # Display menu to select pandemic settings (default or custom)
        print(Fore.BLUE + "*------- [Pandemic Selection] -------*" + Fore.RESET)
        print(Fore.BLUE + "|                                    |" + Fore.RESET)
        print(Fore.BLUE + "| 1. Default Pandemic                |" + Fore.RESET)
        print(Fore.BLUE + "| 2. Configured Pandemic             |" + Fore.RESET)
        print(Fore.BLUE + "*------------------------------------*" + Fore.RESET)
        optionSimulated = self.chooseOption(1, 2, False)
        pandemic = Pandemic(network)
        if optionSimulated == 2:
            print(Fore.BLUE + "Set a number of steps" + Fore.RESET)
            pandemic.steps = self.chooseOption(1, 9, False)
            print(Fore.BLUE + "Set probability of infection" + Fore.RESET)
            pandemic.infection = self.chooseOption(0, 1, True)
            print(Fore.BLUE + "Set probability of recovery" + Fore.RESET)
            pandemic.recovery = self.chooseOption(0, 1, True)
        return pandemic

    def menu_show_configuration_pandemic(self, pandemic):
        # Display the current pandemic configuration
        width = 48
        title = " Pandemic Settings "
        title_bar = f"*{title.center(width - 2, '-')}*"
        print(Fore.BLUE + title_bar + Fore.RESET)
        print(Fore.BLUE + f"|{' ' * (width - 2)}|" + Fore.RESET)
        line1 = f"Steps: {pandemic.steps}"
        line2 = f"Infection probability: {pandemic.infection}"
        line3 = f"Recovery probability: {pandemic.recovery}"
        print(Fore.BLUE + f"| {line1.ljust(width - 3)}|" + Fore.RESET)
        print(Fore.BLUE + f"| {line2.ljust(width - 3)}|" + Fore.RESET)
        print(Fore.BLUE + f"| {line3.ljust(width - 3)}|" + Fore.RESET)
        print(Fore.BLUE + f"*{'-' * (width - 2)}*" + Fore.RESET)

    def chooseOption(self, min_val, max_val, is_decimal):
        # Request a valid option from the user within given bounds
        while True:
            try:
                value = input(Fore.YELLOW + f"Choose option between {min_val}-{max_val}: " + Fore.RESET)
                option = float(value) if is_decimal else int(value)
                if option < min_val or option > max_val:
                    print(f"{Fore.RED}❌ Error: '{option}' is not a valid option{Fore.RESET}")
                else:
                    return int(option) if not is_decimal else option
            except ValueError:
                print(f"{Fore.RED}❌ Error: '{value}' is not a valid option{Fore.RESET}")
    
    def clean(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def press_to_continue(self):
        # Wait for user to press Enter to continue
        input(Fore.YELLOW + "👉 Press enter key to continue..." + Fore.RESET)
        
    def error_message(self, message):
        # Print an error message in red
        print(Fore.RED + message + Fore.RESET)
