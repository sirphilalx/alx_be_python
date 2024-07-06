# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit



temp = int(input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()
# if type(temp) not in [int, float] or unit not in ['C', 'c', 'F', 'f']:
#     temperature = '"Invalid temperature. Please enter a numeric value."'
if unit == 'f':
    temperature = convert_to_celsius(temp)
elif unit == 'c':
    temperature = convert_to_fahrenheit(temp)
else:
    temperature = '"Invalid temperature. Please enter a numeric value."'

print(temperature)