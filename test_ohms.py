from ohms_law import calc_resistance
result = calc_resistance(24, 2)
print("Resistance =", result, "ohms")
print(calc_resistance.__doc__)

# calc_resistance(10, 0)

assert calc_resistance(9, 0.03) == 300
assert calc_resistance(24, 2) == 12