#!/usr/bin/env python3
"""
Program will print out converted values of altitude, velocity and temperature given by the user input.
"""

altitude = input("Enter altitude [meter]: ") # Ber användaren mata in höjd över havet
velocity = input("Indicate velocity [km/h]: ") # Ber användaren mata in hastigheten
temperature = input("Enter temperature outside the plane: ")

#performing conversion
convert_altitude = int(altitude) * 3.28084
convert_velocity = int(velocity) * 0.62137
convert_temperature = int(temperature) * 9/5 + 32

display_value1 = "Current altitude: " + str(convert_altitude)
display_value2 = "Current velocity: " + str(convert_velocity)
display_value3 = "Current tempreture: " + str(convert_temperature)
#Print out converted values
print(display_value1)
print(display_value2)
print(display_value3)
