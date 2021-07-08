# created by Sresha Ventrapragada and Crystal Liang
print("Welcome to the Time Zone Calculator!")
print("Time Zones: PT, MT, CT, ET, AK, HAST")

timezoneDict = {
    "PT": 0,
    "MT": 1,
    "CT": 2,
    "ET": 3,
    "AK": 4,
    "HAST": 5,
}
currentTime = input("Enter your current time: ")
currentTZ = timezoneDict.get(input("Enter your time zone abbreviation: ").upper())
inputDesiredTZ = input("Enter your desired time zone abbreviation: ").upper()
desiredTZ = timezoneDict.get(inputDesiredTZ.upper())
print("Converting...")
timeComparisons = [
    [0, 1, 2, 3, 4, 5],
    [-1, 0, 1, 2, 3, 4],
    [-2, -1, 0, 1, 2, 3],
    [-3, -2, -1, 0, 1, 2],
    [-4, -3, -2, 1, 0, 1],
    [-5, -4, -3, -2, -1, 0]
]

totalMins = 0

if len(currentTime) == 5:
    current_hour = int(currentTime[0:2])
    current_min = int(currentTime[3:5])
    totalMins = (current_hour * 60) + current_min
elif len(currentTime) == 4:
    current_hour = int(currentTime[0:1])
    current_min = int(currentTime[2:4])
    totalMins = (current_hour * 60) + current_min

desiredTotalMins = totalMins + ((timeComparisons[currentTZ][desiredTZ]) * 60)
desiredHours = desiredTotalMins / 60
desiredMins = desiredTotalMins % 60
if(desiredHours > 12):
    desiredHours -= 12
if(desiredHours < 1):
    desiredHours += 12    
print(str(int(desiredHours)) + ":" + str(desiredMins) + " " + inputDesiredTZ)
