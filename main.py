isSimulated = True
def main():
    global isSimulated
    option = 0
    while not option == 4:
        option = showMainMenu()
        if option == 1:
            typeNet = showNetworks()
            isSimulated =True
            simulationNetwork(typeNet)
        if option == 2:
            typeNet = showNetworks()
            isSimulated = False
            simulationNetwork(typeNet)
        if option == 3:
            print("showPandemicEvolution()")

def simulationNetwork(typeNet):
    if typeNet == 1:
        simulationErdosRenyi()
    if typeNet == 2:
        simulationWatts()
    if typeNet == 3:
        simulationBarabasi()    

def simulationErdosRenyi():
    global isSimulated
    nodes = 10
    probability = 0.3
    
    if not isSimulated:
        print("Set number of nodes (N)")
        nodes = chooseOption(1, 100, False)
        
        print("Set probability of two nodes connection (P)")
        probability = chooseOption(0, 1, True)


    print("Network Erdős-Rényi configured:")
    print(f"\tNumber of nodes set (N): {nodes}")
    print(f"\tProbability that and edge exist between two nodes set (P): {probability}")

def simulationWatts():
    nodes = 10
    k = 4
    probabilityRewired = 0.3
    
    if not isSimulated:
        print("Set number of nodes (N)")
        nodes = chooseOption(1, 100, False)
        k = -1
        print("Number of nearest neighbors each node is initially connected to (K)")
        while k < 0 or k >= nodes or k % 2 != 0:
            k = chooseOption(0,nodes,False)
            if k < 0 or k >= nodes or k % 2 != 0:
                print(f"\033[91m❌ k must be greater or equal 0, smaller than nodes and even '{k}' is not a valid option\033[0m")
            
        print("Set rewire probability (P)")
        probabilityRewired = chooseOption(0, 1, True)

    print("Network Watts-Strogatz configured:")
    print(f"\tNumber of nodes set (N): {nodes}")
    print(f"\tNumber of nearest neighbors each node is initially connected to (K): {k}")
    print(f"\tRewire Probability set (P): {probabilityRewired}")
    
    
def simulationBarabasi():
    global isSimulated
    nodes = 10
    m = 2
    if not isSimulated:
        print("Set number of nodes (N)")
        nodes = chooseOption(1, 100, False)
        print("Number of edges to attach from each new node (M)")
        m = chooseOption(1,nodes,False)
        
    print("Network Watts-Strogatz configured:")
    print(f"\tNumber of nodes set (N): {nodes}")
    print(f"\tNumber of edges to attach from each new node (M): {m}")
    
    

def showMainMenu():
    print("Network Simulator")
    print("1. Network Simulation")
    print("2. Network configuration")
    print("3. Show pandemic evolution")
    print("4. Exit")
    option = chooseOption(1,4, False)
    return option

def showNetworks():
    print("1. Erdős-Rényi")
    print("2. Watts-Strogatz")
    print("3. Barabási-Albert")
    option = chooseOption(1,3, False)
    return option    

def chooseOption(min_val, max_val, is_decimal):
    while True:
        try:
            value = input(f"Choose option between {min_val}-{max_val}: ")

            option = float(value) if is_decimal else int(value)

            if option < min_val or option > max_val:
                print(f"\033[91m❌ Error: '{option}' is not a valid option\033[0m")
            else:
                return int(option) if not is_decimal else option

        except ValueError:
            print(f"\033[91m❌ Error: '{value}' is not a valid option\033[0m")

if __name__ == "__main__":
    main()
