#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from infoFromFiles import *
from dateTime import *
from constants import *

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
	newSchedule = []
	oldScheduleList = previousSched
	oldDoctorsList = doctors
	requestsList = requests
	#currentUpdateTime = nextTime = requests[-9:-4]
	oldTimes = []
	for schedule in oldScheduleList:
		for oldTime in range(len(schedule)):
			if oldTime == 0:
				oldTimes.append(schedule[oldTime])

	oldDoctorsTime = {}
	for doctor in oldDoctorsList:
		for _ in doctor:
			oldDoctorsTime[doctor[DOCT_NAME_IDX]] = doctor[DOCT_BIRTH_END_IDX]

	doctorsSkills = {}
	for doctor in oldDoctorsList:
		for _ in doctor:
			doctorsSkills[doctor[DOCT_NAME_IDX]] = doctor[DOCT_SKILL_IDX]

	requestsRisks = {}
	for request in requestsList:
		for _ in request:
			requestsRisks[request[MOTH_NAME_IDX]] = request[MOTH_RISK_IDX]

	assignedDoctor = None
	momDoctor = {}
	highMoms = []

	for momName, risk in requestsRisks.items():
		if risk == "high":
			highMoms.append(momName)
			print(highMoms)
			for name, skill in doctorsSkills.items():
				if int(skill) >= 2:
					assignedDoctor = name
					for mom in highMoms:
						momDoctor[assignedDoctor] = mom
	"""
	oldHeader = saveHeader(previousSched)
	newHeader = []
	for i in range(len(oldHeader)):
		if i == HEADER_TIME_IDX:
			oldHeader[i] == f"{minutesToInt(oldHeader[i]) + 30}"
		newHeader.append(i)"""

	return momDoctor

print(updateSchedule("doctors10h00.txt", "requests10h30.txt", "schedule10h00.txt", "10h30"))


def updateDoctors(doctors, requests, previousSched, nextTime):
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
	












