def main():
    option = 0
    while not option == 4:
        option = showMainMenu()
        if option == 1:
            typeNet = showNetworks()
            
        if option == 2:
            typeNet = showNetworks()
            
        if option == 3:
            print("#showPandemicEvolution()")
               
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
