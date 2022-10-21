import random

alarm_data = []
alarm_list = [
    "Band Alarm",
    "Beach Alarm",
    "Calming Alarm",
    "Celestial Alarm",
    "Galaxy Alarm",
    "Happy Alarm",
    "March Alarm",
    "Soulful Alarm",
    "Space Alarm",
    "Traditional Alarm"
]

# Initialize alarms
def initAlarms():
    # setup alarms into a dictionary with id, alarm, likes, dislikes
    item_id = 0
    for item in alarm_list:
        alarm_data.append({"id": item_id, "alarm": item, "likes": 0, "dislikes": 0})
        item_id += 1
        
# Return all alarms from alarm_data
def getAlarms():
    return(alarm_data)

# alarm getter
def getalarm(id):
    return(alarm_data[id])

# Return random alarm from alarm_data
def getRandomAlarm():
    return(random.choice(alarm_data))

# Liked alarm
def favoriteAlarm():
    best = 0
    bestID = -1
    for alarm in getAlarms():
        if alarm['likes'] > best:
            best = alarm['likes']
            bestID = alarm['id']
    return alarm_data[bestID]
    
# Disliked alarm
def worstAlarm():
    worst = 0
    worstID = -1
    for alarm in getAlarms():
        if alarm['dislikes'] > worst:
            worst = alarm['dislikes']
            worstID = alarm['id']
    return alarm_data[worstID]

# Add to likes for requested id
def addAlarmVote(id):
    alarm_data[id]['likes'] = alarm_data[id]['likes'] + 1
    return alarm_data[id]['likes']

# Add to dislikes for requested id
def addAlarmDislike(id):
    alarm_data[id]['dislikes'] = alarm_data[id]['dislikes'] + 1
    return alarm_data[id]['dislikes']

# Pretty Print alarm
def printAlarm(alarm):
    print(alarm['id'], alarm['alarm'], "\n", "likes:", alarm['likes'], "\n", "dislikes:", alarm['dislikes'], "\n")

# Number of alarms
def countAlarms():
    return len(alarm_data)

# Test alarm Model
if __name__ == "__main__": 
    initAlarms()  # initialize alarms
    
    # Most likes and most dislikes
    best = favoriteAlarm()
    print("Most liked", best['likes'])
    printAlarm(best)
    worst = worstAlarm()
    print("Most disliked", worst['dislikes'])
    printAlarm(worst)
    
    # Random alarm
    print("Random alarm")
    printAlarm(getRandomAlarm())
    
    # Count of alarms
    print("Slarms Count: " + str(countAlarms()))