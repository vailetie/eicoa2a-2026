def calc_resistance(voltage, current):
    """
    Calculate the electrical resistance using Ohm's Law.
    
    Args:
        voltage (float): The voltage across the component in Volts (V).
        current (float): The current through the component in Amperes (A). Must be non-zero.
    
    Returns:
        float: Resistance in ohms (Ω).
    
    Notes:
        The function raises a ZeroDivisionError if the current is 0.
    """
    return voltage / current

def calc_power(voltage, resistance):
    """
    Calculate power dissipated in a resistor using P = V X I.
    
    Args:
        voltage (float): Voltage across the component in Volts (V).
        resistance (float): The resistance of the component in ohms (Ω). Must be non-zero.
    
    Returns:
        float: Power in watts (W).
    
    Notes:
        Current is derived from Ohm's Law (I = V / R) before calculating power.
    """
    current = voltage / resistance
    power = voltage * current
    return power