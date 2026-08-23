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