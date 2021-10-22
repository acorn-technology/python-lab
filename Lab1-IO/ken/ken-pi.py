import math

user_input = input("How many decimals do you want me to use when showing Pi? ")

no_of_decimals = "." + user_input + "f"
pi_value = format(math.pi, no_of_decimals)

print(f"Pi has the value {pi_value}")
