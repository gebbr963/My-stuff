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

"""
import random
print("===ZENKAI CALCULATOR===")
power_level = int(input("What is your power level? "))
damage = float(input("How much damage did you suffer, on a scale from 1 to 100? "))
potential = random.randrange(1,10) 
weakling_zenkai = (power_level*1.5)+1/50*(damage*potential)
average_zenkai = (power_level*2.25)+1/50*(damage*potential)
sparking_zenkai = (power_level*5)+1/50*(damage*potential)
if power_level < 4000:
    print(f"Your power is {power_level}? ...scum.")
    print(f"Your total power level is {int(round(weakling_zenkai + power_level, 0))}.")
    if weakling_zenkai+power_level > 2*power_level:
        print("Maybe now you'll be worth something after all...")
elif power_level < 530000:
    print(f"Your total power level is {int(round(average_zenkai + power_level, 0))}.")
    if average_zenkai+power_level > 2.5*power_level:
        print("You've come a long way.")
else:
    print(f"{power_level}?! Amazing!  I've yet to seen a power greater than that of lord Freeza!")
    print(f"Your total power level is {int(round(sparking_zenkai + power_level, 0))}.")
    if sparking_zenkai+power_level > 2.5*power_level:
        print("Incredible! What latent potential!")
"""
