print("===ZENKAI CALCULATOR===")

import random
power_level = int(input("What is your power level? "))
damage = float(input("How much damage did you suffer, on a scale from 1 to 100? "))
potential = random.randrange(1,10) 
weakling_zenkai = (power_level*1.5)/(damage/potential)
average_zenkai = (power_level*2.25)/(damage/potential)
sparking_zenkai = (power_level*5)/(damage/potential)
if power_level < 4000:
    print(f"Your power is {power_level}? ...scum.")
    print(f"Your total power level is {weakling_zenkai + power_level}.")
elif power_level < 530000:
    print(f"Your total power level is {average_zenkai + power_level}.")
else:
    print(f"Amazing!  I've yet to seen a power greater than {power_level}!")
    print(f"Your total power level is {sparking_zenkai + power_level}.")