from menu import Menu

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
            print("showPandemicEvolution()")
            
    print("FIN DEL PROGRAMA")   
            
if __name__ == "__main__":
    main()