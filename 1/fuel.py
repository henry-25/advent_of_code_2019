import math

# Part 1

# total_fuel = 0
#
# with open('input.txt') as file:
#     for line in file:
#         mass = int(line)
#         fuel = math.floor(mass/3) - 2
#         total_fuel += fuel


# Part 2

total_mass_fuel = 0

with open('input.txt') as file:
    for line in file:
        mass = int(line)
        fuel = math.floor(mass/3) - 2
        while fuel > 0:
            total_mass_fuel += fuel
            extra_fuel = math.floor(fuel/3) - 2
            fuel = extra_fuel

print(total_mass_fuel)
