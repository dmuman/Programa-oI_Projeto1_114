#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from infoFromFiles import *
from dateTime import *
from constants import *


#function for sorting the requests
def sortRequests(requestlist):
	"""
    Sorts mothers(i.e. requests) in decrescent order of risks. 
    If they're the same - in decrescent order of tags. 
    If they're the same - in decrescent order of age. 
    If they're the same - in alphabetical order of names.

    Requires: requestList is a list of list, each list represents a mother(i.e. request).

    Ensures: tuple, containing the risk, tag, age and name of the corresponding mother(i.e. request).
	"""
	risks={"high":1, "low":2}                   #creating dictionary with risks and corresponding integers
	tags={"red": 3, "yellow":2, "green":1}      #creating dictionary with tags and corresponding integers

	return (-risks[requestlist[MOTH_RISK_IDX]], tags[requestlist[MOTH_TAG_IDX]],\
          -int(requestlist[MOTH_AGE_IDX]), requestlist[MOTH_NAME_IDX])      #returning risk, tag, age and name


#function for sorting the doctors
def sortDoctors(doctorsList):
    """
    Sorts doctors in decrescent order of their skills.
    If they're the same - in decrescent order of time that's left until 1 hour pause.
    If they're the same - in decrescent order of time that's left until weekly leave.
    If they're the same - in the alphabetical order of the names.

    Requires: doctorsList is a list of list, each list represents a doctor.

    Ensures: tuple, containing the skill, time left unti 1 hour pause, 
    time left unti weekly leave and name of the corresponding doctor.
    """
    if int(doctorsList[DOCT_DAILY_HOURS_IDX]) > 240:                    #checks if the daily worked minutes are greater than 240
        timeToPause = 240*2 - int(doctorsList[DOCT_DAILY_HOURS_IDX])    #if so, timeToPause will be 240*2(i.e. limit times 2) - daily worked minutes
    else:                                                               #if it's not greater than 240(i.e. less than 240)
        timeToPause = 240 - int(doctorsList[DOCT_DAILY_HOURS_IDX])      #timeToPause will be 240(i.e. limit) - daily worked minutes

    totalMinutesWeeklyWorked = (hourToInt(doctorsList[DOCT_REST_HOURS_IDX]) * 60 \
                    + minutesToInt(doctorsList[DOCT_REST_HOURS_IDX]))   #gaining totalMinutes for weekly work
    
    timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked              #calculating the time left until weekly pause

    return (-int(doctorsList[DOCT_SKILL_IDX]), -timeToPause, \
            -timeToWeeklyPause, doctorsList[DOCT_NAME_IDX])             #returning skill, time left to one hour pause, time left to weekly pause and the name


#function for sorting the schedule
def sortSchedule(scheduleList):
    """
    Sorts schedule in crescent order of schedule's time.
    If they're the same - in alphabetical order of mother's name.
    If they're the same - in alphabetical order of doctor's name.

    Reqires: scheduleList is a list of lists, each list represents a schedule.

    Ensures: tuple, containing the time of the schedule(total), 
    name of the corresponding mother and name of the corresponding doctor.
    """
    totalTime = hourToInt(scheduleList[0])*60 + minutesToInt(scheduleList[0])   #calculating total time of the assigment hour
    
    return totalTime, scheduleList[MOTH_NAME_IDX], scheduleList[DOCT_NAME_IDX]  #returning totalTime, mother's name and doctor's name


#function for updating the schedule
def updateSchedule(doctors, requests, previousSched, nextTime):
    """
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	nextTime is a string in the format HHhMM with the time of the next schedule

	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
    """
    #declaring variables for assigned hours and doctor
    horasAssigned = None
    doctorAssigned = None
    
    #declaring cariable for the new schedule list
    newScheduleList = []

    #part for redirecting to the other network if hours are greater then 20
    for assignedTimeFromOldSchedule in readScheduleFile(previousSched):                         #reading and searching through the previous schedule
        if hourToInt(updateHours(assignedTimeFromOldSchedule[0], 20)) >= 20:                    #ckecks if updated hours from it are greater than 20
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), \
                                      minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))   #assigned hours will be equal to the new schedule time in the header
            doctorAssigned = REDIR_STR                                                          #assigned doctor will be equal to "redirected to other network"

    #part for adding mothers from the old schedule if the time of the appointment 
    #is bigger than the time of the new schedule
    for appointment in readScheduleFile(previousSched):                             #reading and searching through the previous schedule
        if hourToInt(appointment[0]) >= hourToInt(nextTime)\
              and minutesToInt(appointment[0]) >= minutesToInt(nextTime):           #checks if its hours and minutes are greater than the new schedule
            newScheduleList.append(appointment)                                     #if so, this appointment will be added to the new schedule
            
    assignedDoctors = []                                    #declaring variable for assigned doctors list

    mothersList = readRequestsFile(requests)                #declaring variable for old mothers from the previous schedule
    doctorsList = readDoctorsFile(doctors)                  #declaring variable for doctors from the previous doctors
    
    sortedMothers = sorted(mothersList, key=sortRequests)   #declaring variable for sorted mothers
    sortedDoctors = sorted(doctorsList, key=sortDoctors)    #declaring variable for sorted doctors

    for mother in sortedMothers:                            #searching through sorted mothers
        isDoctorAssigned = False                            #declaring variable for the doctor's state

        for doctor in sortedDoctors:                        #searching through sorted doctors
            if ((mother[MOTH_RISK_IDX] == "high" and int(doctor[DOCT_SKILL_IDX]) >= 2 and isDoctorAssigned == False)
                or (mother[MOTH_RISK_IDX] == "low" and int(doctor[DOCT_SKILL_IDX]) >= 1 and isDoctorAssigned == False))\
                         and doctor not in assignedDoctors: #checks if mother's risk is "high" and doctor's skill is greater or equal 2 
                                                            #or mother's risk is "low" and doctor's skill is greater or equal 1
                                                            #and doctor is not yet assigned
                
                horasAssigned = doctor[DOCT_BIRTH_END_IDX]  #if so, assigned hours will be equal to the hours when the doctor is free
                doctorAssigned = doctor[DOCT_NAME_IDX]      #assigned doctor will be equal to the doctor's name
                
                if hourToInt(horasAssigned)*60 + minutesToInt(horasAssigned) < \
                    hourToInt(nextTime)*60 + minutesToInt(nextTime):    #checks if the assigned hours are less than the updated time of the schedule
                    horasAssigned = nextTime                            #if so, assigned hours will be equal to the updated schedule's time

                appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]    #declaring new appointment, containing assigned hours, mother's and doctor's names
                newScheduleList.append(appointment)                                     #appending new schedule list
                assignedDoctors.append(doctor)                                          #appending siigned doctors list
                isDoctorAssigned = True                                                 #making doctor assigned

        if not isDoctorAssigned:                                #checks if doctor is already assigned and there's no free doctors
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), \
                                      minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))   #assigned hours will be equal to the new schedule time in the header
            doctorAssigned = REDIR_STR                                                          #assigned doctor will be equal to "redirected to other network"
            appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]                #declaring new appointment, containing assigned hours, mother's name and redirected string
            newScheduleList.append(appointment)                                                 #appending new schedule list

    newSortedScheduleList = sorted(newScheduleList, key=sortSchedule)   #declaring new, sorted by time schedule 

    return newSortedScheduleList                                        #returning sorted by time schedule                                                        


#function for updating the doctors' time
def updateDoctorsTime(oldDoctor, minutesToAdd):
    """
    Updates the next free time of the corresponding doctor with the given amount of minuts. 
    Checks if the new time is ultrapassing the 240 minutes limit. 
    If so - adding 1 hour to the next free time(i.e. 1 hour pause).
    Also checks if the week worked hours is ultrapassing the 40 hours limit.
    If so - doctor will receive weekly leave(i.e. next free time = "weekly leave")

    Requires: oldDoctor is a list, containing information about corresponding doctor.
    I.e. name, his skill level, next free time, daily minutes worked, weekly hours worked.

    Ensures: updated list that represents new doctor, containing updated next free time, 
    daily worked minutes and weekly worked hours.
    """
    #declaring variables for old free hours, daily minutes worked and weekly hours worked
    oldFreeHours = oldDoctor[DOCT_BIRTH_END_IDX]
    oldMinutesDias = oldDoctor[DOCT_DAILY_HOURS_IDX]
    oldHorasSemanais = oldDoctor[DOCT_REST_HOURS_IDX]

    #declaring variables for new free hours, daily minutes worked and weekly hours worked
    newFreeHours = None
    newHorasSemanais = None
    newMinutesDias = int(oldMinutesDias) + minutesToAdd #already adding minutes to it

    #declaring variables for old hours and minutes from old free hours
    hoursFromOldHours = hourToInt(oldFreeHours)
    minutesFromOldHours = minutesToInt(oldFreeHours)

    if minutesFromOldHours < 30:                                            #checks if minutes from old hours are less then 30(time from the new schedule)
        minutesFromOldHours = minutesToInt(oldFreeHours) + \
            (30 - minutesToInt(oldFreeHours))                               #if so, properly adding new minutes
        oldFreeHours = intToTime(hoursFromOldHours, minutesFromOldHours)    #updating old free hours, considering the time in new schedule
        newFreeHours = updateHours(oldFreeHours, minutesToAdd)              #calculating new free hours, using updateHours() function from the dateTime module
    
    if int(oldMinutesDias) < 240:                                       #checks if old daily minutes worked are less than 240
        if newMinutesDias >= 240:                                       #if so, checks if new daily minutes worked are greater than 240
            newFreeHours = intToTime(hourToInt(oldFreeHours) + 1, \
                                     minutesToInt(oldFreeHours)+20)     #if so, adding one hour(i.e. one hour pause) to the new free hours
        else:                                                           #checks if new daily minutes worked are less than 240
            newFreeHours = updateHours(oldFreeHours, minutesToAdd)      #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
    else:                                                               #checks if old daily minutes worked are already greater than 240
        newFreeHours = updateHours(oldFreeHours, minutesToAdd)          #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
    
    newHorasSemanais = updateHours(oldHorasSemanais, minutesToAdd)      #updating new weekly worked hours using the updateHours() function from the dateTime module

    if hourToInt(newHorasSemanais) >= 40:           #checks if new weekly worked hours are greater than 40
        newFreeHours = WKL_PAUSE                    #if so, doctor receives weekly pause   

    return [oldDoctor[DOCT_NAME_IDX], str(oldDoctor[DOCT_SKILL_IDX]), \
            newFreeHours, str(newMinutesDias), newHorasSemanais]        #returning doctor's name, his skills, new free hours, new daily worked minutes and new weekly worked hours


#function for updating doctors
def updateDoctors(doctors):
    """
    Update the doctors information taking into account a previous doctors information.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	
	Ensures:
	a list of doctors, representing the doctors updated at
	the current update time (= previous update time + 30 minutes),
	according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
    """
    doctorList = readDoctorsFile(doctors)                           #declaring variable and storing info from doctors file using readDoctorsFile() function from the infoFromFiles module
    timeInHeader = saveHeader(doctors)[HEADER_TIME_IDX][0]          #declaring variable for the time in header
    newDoctors = []                                                 #declaring list for new doctors

    for doctor in doctorList:                                       #searching through doctors list
        if hourToInt(doctor[DOCT_BIRTH_END_IDX])*60 + \
            minutesToInt(doctor[DOCT_BIRTH_END_IDX]) < (hourToInt(timeInHeader)+1)*60:  #checks if doctor's old free hours are less than time in the header of old doctors file
            
            doctor = updateDoctorsTime(doctor, 20)      #if so, updating his info with updateDoctorsTime() function
            newDoctors.append(doctor)                   #appending new doctors file
        else:                                           #checks if doctor's old free hours are greater than time in the header of old doctors file
            newDoctors.append(doctor)                   #keeping his old free hours and appending new doctors file

    return newDoctors       #returning list with updated doctors
