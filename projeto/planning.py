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
    Sorts mothers
	"""
	risks={"high":1, "low":2}
	tags={"red": 3, "yellow":2, "green":1}
	return (-risks[requestlist[MOTH_RISK_IDX]], tags[requestlist[MOTH_TAG_IDX]],\
          -int(requestlist[MOTH_AGE_IDX]), requestlist[MOTH_NAME_IDX])


def sortDoctors(doctorsList):
    """
    Sorts doctors
    """
    
    if int(doctorsList[DOCT_DAILY_HOURS_IDX]) > 240:
        timeToPause = 240*2 - int(doctorsList[DOCT_DAILY_HOURS_IDX])
    else:
        timeToPause = 240 - int(doctorsList[DOCT_DAILY_HOURS_IDX])
    timeToWeeklyPause = 40 * 60 - (hourToInt(doctorsList[DOCT_REST_HOURS_IDX]) * 60 + minutesToInt(doctorsList[DOCT_REST_HOURS_IDX]))

    return (-int(doctorsList[DOCT_SKILL_IDX]), -timeToPause, -timeToWeeklyPause, doctorsList[DOCT_NAME_IDX])

def sortSchedule(scheduleList):
    """
    Sorts schedule  
    """
    totalTime = None
    if scheduleList[0] == REDIR_HOURS:
        totalTime = hourToInt("23h59")*60 + minutesToInt("23h59")
    else:
        totalTime = hourToInt(scheduleList[0])*60 + minutesToInt(scheduleList[0])
    
    return totalTime

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

    #part for redirecting to the other network (works great)
    for assignedTimeFromOldSchedule in readScheduleFile(previousSched):
        if hourToInt(updateHours(assignedTimeFromOldSchedule[0], 20)) >= 20:
            horasAssigned = REDIR_HOURS
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
            horasAssigned = REDIR_HOURS
            doctorAssigned = REDIR_STR
            appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]
            newScheduleList.append(appointment)
    newSortedScheduleList = sorted(newScheduleList, key=sortSchedule)
    return newSortedScheduleList

#print(updateSchedule("doctors14h00.txt", "requests14h30.txt", "schedule14h00.txt", "14h30"))

def updateDoctorsTime(oldDoctor, minutesToAdd):
    """
    
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
