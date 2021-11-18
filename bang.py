# The Bang-Out-O-Meter
# Jack Tench, 2021

# Instructions
# ------------
# Get JSON from on.spiceworks.com/api/tickets.json
# Place in the same folder as this python script, and then run.
# The bang-out-o-meter will measure the levels for you, automatically.

# A lot of this is stolen from various people on the internet. idk don't ask me, it works
# Ryan Strassberger (https://gist.github.com/ryanstrass/5502075)
# JSON Parser (http://json.parser.online.fr/)

# Imports
import json
import os
import time

# Defaults.
opentickets = 0 # Starts the counter of open tickets at 0.
spiceworks = "tickets.json" # Path to the JSON from spiceworks.

# Ensure the JSON from spiceworks exists.
if os.path.exists(spiceworks):
    #print("We're in the money!")
    time.sleep(0.5)
else:
    #print("Nope! I'm out!")
    exit()

# Open and load the JSON file.
rawjsonfile = open(spiceworks)
rawjson = json.load(rawjsonfile)

# Test code. Spits out raw JSON. Ew, ugly.
#print(str(rawjson))

# Cycle through every ticket in the JSON.
for ticket in rawjson['tickets']:
    
    # Detect if a ticket is open or waiting, then iterate the count.
    if ticket["status"] == "open":
        #print("open")
        opentickets += 1
    elif ticket["status"] == "waiting":
        #print("waiting")
        opentickets += 1

# Test code. Prints the number of tickets that are set to open/waiting.
#print(str(opentickets))

# Test code. Used to force a certain result after the count. STOP THE VOTE!
#opentickets = 20

# Let's make things pretty. Header.
print("The Bang-Out-O-Meter")
print("--------------------")

# Print the results.
# Low levels.
if opentickets <= 3:
    print("The bang out levels are reasonably low today. You're in the clear.")
    print("You have " + str(opentickets) + " tickets open. No need to bang anyone out just yet.")

# Medium levels.
if 3 < opentickets <= 6:
    print("The bang out levels are starting to rise. Be worried.")
    print("You have " + str(opentickets) + " tickets open.")
    print("You'd better get them down before you need to resort to banging sombody out.")

# High levels.
if 6 < opentickets <= 10:
    print("The bang out levels are very high today. Boxing gloves at the ready.")
    print("You have " + str(opentickets) + " tickets open.")

# Extremely high levels.
if opentickets > 10:
    print("The bang out levels are off the scale! Break out the knuckle dusters!")
    print("You have " + str(opentickets) + " tickets open. You're facing jail time at this point.")
    
while True:
    time.sleep(20)
