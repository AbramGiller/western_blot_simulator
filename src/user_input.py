def get_lanes():
    while True:
        try:
            lanes = int(input("Enter the number of lanes: "))
            if lanes > 0:
                return lanes
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

