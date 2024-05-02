# Temp unit converter

# Define conversion functions
def C_to_F(value):
    """Celsius to Fahrenheit"""
    return (value * 9/5) + 32

def F_to_C(value):
    """Fahrenheit to Celsius"""
    return (value - 32) * 5/9

# Get input from user
units = input("What unit would you like to convert to? (answer C or F): ")
value = float(input("What temperature would you like to convert?: "))

# Perform conversion
if units.upper() == "C":
    print(f"{value} Degrees Celsius is {C_to_F(value):.2f} Fahrenheit.")
elif units.upper() == "F": 
    print(f"{value} Degrees Fahrenheit is {F_to_C(value):.2f} Celsius.")
else: 
    print("Incorrect input, please choose C or F.")