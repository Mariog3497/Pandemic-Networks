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
