from menu import Menu
from pandemic import Pandemic

def main():
    menu = Menu()
    option = 0
    network = None
    while not option == 4:
        option = menu.main()
        if option == 1:
            network = menu.networks()
            network.configuration()
        if option == 2:
            if network!=None:
                print(network)
            else:
                print("You must first configurate your network")
        if option == 3:
            if network!=None:
                pandemic = Pandemic(0.7, 0.3, 10,network)
                pandemic.showPandemicEvolution()
            else:
                print("You must first configurate your network")

            
    print("EXIT")   
            
if __name__ == "__main__":
    main()