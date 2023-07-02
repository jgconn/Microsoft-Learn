from datetime import date;

#sums
sum = 1 + 2;
print(sum)

planets_in_solar_system = 8
distance_to_alpha_centauri = 4.367 
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11"

print(date.today())
print("Todays date is:", date.today())

# name = input("Enter your name: ")
# print(name)

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

if a == 34 and b == 34:
    print (a + b)

# + doesn't work , you can create a new variable
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)

fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# uppercase every first letter for every word
print("temperatures and facts about the moon".title())

# string split
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

# searching in a string
print("Moon" in "This text will describe facts and challenges with space travel")

# using find() for specific word index
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

# count() counts occurance of word
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

# find if numeric; this would print 30
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# return true if starts with
print("-60".startswith('-'))

# return true if ends with
if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# replace
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

# join all var in list
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

# % sign formatting
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# format() method
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

# improve readable
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

# f-string format
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

# don't assign variable
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

# math lib
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# lists planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# pop()
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# reverse 
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# find a value in list
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# join lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

