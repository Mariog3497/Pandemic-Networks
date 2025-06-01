from util import chooseOption
from network import *
class Menu:
    def main(self):
        print("Network Simulator")
        print("1. Network Settings")
        print("2. Show Network configuration")
        print("3. Show pandemic evolution")
        print("4. Exit")
        option = chooseOption(1,4, False)
        return option
    
    def networks(self):
        print("1. Erdős-Rényi")
        print("2. Watts-Strogatz")
        print("3. Barabási-Albert")
        network = None
        typeNetwork = chooseOption(1,3, False)
        
        print("Choose between 1. default or 2. configured network")
        simulated = False
        optionSimulated = chooseOption(1,2, False)

        if optionSimulated == 1:
            simulated = True
        
        if typeNetwork == 1:
            network = ErdosRenyi(simulated)
        if typeNetwork == 2:
            network = WattsStrogatz(simulated)
        if typeNetwork == 3:
            network = BarabasiAlbert(simulated)
        return network