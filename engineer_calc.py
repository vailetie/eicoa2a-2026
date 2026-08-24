from ohms_law import calc_resistance
from unit_converter import mm_to_inches, inches_to_mm
def display_menu():
    """Print a numbered menu of engineering calculations.
    the menu includes 
    1. Calculate resistance (Ohms Law)
    2. Convert length ( mm <-> inches )
    3. Exit
    """
print("\n--- Engineering Calculator Menu ---")
print("1. Calculate resistance")
print("2. Convert length")
print("3. Exit")
def main():
    running = True
    while running:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            resistance = calc_resistance(voltage, current)
            print("Resistance =", resistance, "ohms")
        elif choice == "2":
            direction = input("Enter conversion (mm_to_in or in_to_mm): ")
            value = float(input("Enter the measurement: "))
            if direction == "mm_to_in":
                result = mm_to_inches(value)
                print("Converted value:", result, "inches")
            elif direction == "in_to_mm":
                result = inches_to_mm(value)
                print("Converted value:", result, "mm")
            else:
                print("Invalid conversion option.")
        elif choice == "3":
            print("Exiting the calculator. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)