#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from infoFromFiles import *
from dateTime import *
from constants import *

def sortRequests(requestlist):
	"""
    Sorts mothers(i.e. requests) in decrescent order of risks. 
    If they're the same - in decrescent order of tags. 
    If they're the same - in decrescent order of age. 
    If they're the same - in alphabetical order of names.

    Requires: requestList is a list of list, each list represents a mother(i.e. request).

    Ensures: tuple, containing the risk, tag, age and name of the corresponding mother(i.e. request).
	"""
	risks={"high":1, "low":2}
	tags={"red": 3, "yellow":2, "green":1}
	return (-risks[requestlist[MOTH_RISK_IDX]], tags[requestlist[MOTH_TAG_IDX]],\
          -int(requestlist[MOTH_AGE_IDX]), requestlist[MOTH_NAME_IDX])


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
    
    if int(doctorsList[DOCT_DAILY_HOURS_IDX]) > 240:
        timeToPause = 240*2 - int(doctorsList[DOCT_DAILY_HOURS_IDX])
    else:
        timeToPause = 240 - int(doctorsList[DOCT_DAILY_HOURS_IDX])
    timeToWeeklyPause = 40 * 60 - (hourToInt(doctorsList[DOCT_REST_HOURS_IDX]) * 60 + minutesToInt(doctorsList[DOCT_REST_HOURS_IDX]))

    return (-int(doctorsList[DOCT_SKILL_IDX]), -timeToPause, -timeToWeeklyPause, doctorsList[DOCT_NAME_IDX])


def sortSchedule(scheduleList):
    """
    Sorts schedule in crescent order of schedule's time.
    If they're the same - in alphabetical order of mother's name.
    If they're the same - in alphabetical order of doctor's name.

    Reqires: scheduleList is a list of lists, each list represents a schedule.

    Ensures: tuple, containing the time of the schedule(total), 
    name of the corresponding mother and name of the corresponding doctor.
    """
    totalTime = hourToInt(scheduleList[0])*60 + minutesToInt(scheduleList[0])
    
    return totalTime, scheduleList[MOTH_NAME_IDX], scheduleList[DOCT_NAME_IDX]


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
    horasAssigned = None
    doctorAssigned = None
    
    newScheduleList = []

    #part for redirecting to the other network if hours are greater then 20 (works great)
    for assignedTimeFromOldSchedule in readScheduleFile(previousSched):
        if hourToInt(updateHours(assignedTimeFromOldSchedule[0], 20)) >= 20:
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))
            doctorAssigned = REDIR_STR

    #part for adding mothers from the old schedule if the time of the appointment 
    #is bigger than the time of the new schedule (works great)
    for appointment in readScheduleFile(previousSched):
        if hourToInt(appointment[0]) >= hourToInt(nextTime)\
              and minutesToInt(appointment[0]) >= minutesToInt(nextTime):
            newScheduleList.append(appointment)
            
    assignedDoctors = []

    mothersList = readRequestsFile(requests)
    doctorsList = readDoctorsFile(doctors)
    
    sortedMothers = sorted(mothersList, key=sortRequests)
    sortedDoctors = sorted(doctorsList, key=sortDoctors)

    for mother in sortedMothers:
        isDoctorAssigned = False

        for doctor in sortedDoctors:
            if ((mother[MOTH_RISK_IDX] == "high" and int(doctor[DOCT_SKILL_IDX]) >= 2 and isDoctorAssigned == False)
                or (mother[MOTH_RISK_IDX] == "low" and int(doctor[DOCT_SKILL_IDX]) >= 1 and isDoctorAssigned == False))\
                         and doctor not in assignedDoctors:
                horasAssigned = doctor[DOCT_BIRTH_END_IDX]
                doctorAssigned = doctor[DOCT_NAME_IDX]
                
                if hourToInt(horasAssigned)*60 + minutesToInt(horasAssigned) < hourToInt(nextTime)*60 + minutesToInt(nextTime):
                    horasAssigned = nextTime
                appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]
                newScheduleList.append(appointment)
                assignedDoctors.append(doctor)
                isDoctorAssigned = True

        if not isDoctorAssigned:
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))
            doctorAssigned = REDIR_STR
            appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]
            newScheduleList.append(appointment)
    newSortedScheduleList = sorted(newScheduleList, key=sortSchedule)
    return newSortedScheduleList


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
    oldFreeHours = oldDoctor[DOCT_BIRTH_END_IDX]
    oldMinutesDias = oldDoctor[DOCT_DAILY_HOURS_IDX]
    oldHorasSemanais = oldDoctor[DOCT_REST_HOURS_IDX]
    newFreeHours = None
    newHorasSemanais = None
    newMinutesDias = int(oldMinutesDias) + minutesToAdd
    hoursFromOldHours = hourToInt(oldFreeHours)
    minutesFromOldHours = minutesToInt(oldFreeHours)

    if minutesFromOldHours < 30:
        minutesFromOldHours = minutesToInt(oldFreeHours) + (30 - minutesToInt(oldFreeHours))
        oldFreeHours = intToTime(hoursFromOldHours, minutesFromOldHours)
        newFreeHours = updateHours(oldFreeHours, minutesToAdd)
    
    if int(oldMinutesDias) < 240:
        if newMinutesDias >= 240:
            newFreeHours = intToTime(hourToInt(oldFreeHours) + 1, minutesToInt(oldFreeHours)+20)
        else:
            newFreeHours = updateHours(oldFreeHours, minutesToAdd)
    else:
        newFreeHours = updateHours(oldFreeHours, minutesToAdd)
    
    newHorasSemanais = updateHours(oldHorasSemanais, minutesToAdd)

    if hourToInt(newHorasSemanais) >= 40:
        newFreeHours = WKL_PAUSE

    return [oldDoctor[DOCT_NAME_IDX], str(oldDoctor[DOCT_SKILL_IDX]), newFreeHours, str(newMinutesDias), newHorasSemanais]


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
    doctorList = readDoctorsFile(doctors)
    timeInHeader = saveHeader(doctors)[HEADER_TIME_IDX][0]
    newDoctors = []
    for doctor in doctorList:
        if hourToInt(doctor[DOCT_BIRTH_END_IDX])*60 + minutesToInt(doctor[DOCT_BIRTH_END_IDX]) < (hourToInt(timeInHeader)+1)*60:
            doctor = updateDoctorsTime(doctor, 20)
            newDoctors.append(doctor)
        else:
            newDoctors.append(doctor)
    return newDoctors
