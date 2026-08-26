from ohms_law import calc_resistance
from unit_converter import mm_to_inches, inches_to_mm, cm_to_inches, inches_to_cm
DEFAULT_CURRENT = 0.5
print("Global value:", DEFAULT_CURRENT)
def build_menu():
    """Return the list of menu option labels for the engineering calculator."""
    options = [
        "Calculate Resistance",
        "Convert mm to inches",
        "Convert inches to mm",
        "Convert cm to inches",
        "Convert inches to cm",
        "Exit"
    ]
    return options
def display_menu():
   """Print the numbered engineering calculator menu using build_menu()."""
   print("\n--- Engineering Calculator Menu ---")
   options = build_menu()
   for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])
def show_default():
    DEFAULT_CURRENT = 1.0
    print("Inside function:", DEFAULT_CURRENT)
def main():
    running = True
    while running:
        display_menu()
        show_default()
        print("Outside function:", DEFAULT_CURRENT)
        choice = input("Select an option: ")
        if choice == "1":
                voltage = float(input("Enter voltage (V): "))
                current = input("Enter current (A) or press Enter for default: ")
                if current == "":
                    current = DEFAULT_CURRENT
                else:
                    current = float(current)
                try:
                  resistance = calc_resistance(voltage, current)
                  print("Resistance =", resistance, "ohms")
                except ZeroDivisionError:
                    print("Error: Current cannot be zero.") 
        elif choice == "2":
            direction = input("Enter conversion (mm_to_in, in_to_mm, cm_to_in, in_to_cm): ")
            value = float(input("Enter the measurement: "))
            if direction == "mm_to_in":
                result = mm_to_inches(value)
                print("Converted value:", result, "inches")
            elif direction == "in_to_mm":
                result = inches_to_mm(value)
                print("Converted value:", result, "mm")
            elif direction == "cm_to_in":
                result = cm_to_inches(value)
                print("Converted value:", result, "inches")
            elif direction == "in_to_cm":
                result = inches_to_cm(value)
                print("Converted value:", result, "cm")
            else:
                print("Invalid conversion option.")
        elif choice == "6":
            print("Exiting the calculator. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)