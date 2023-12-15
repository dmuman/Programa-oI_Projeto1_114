from constants import *
from testAddingTimes import *
from infoFromFiles import *

def sortRequests(requestlist):
	"""
    Sorts mothers
	"""
	risks={"high":1, "low":2}
	tags={"red": 3, "yellow":2, "green":1}
	return (risks[requestlist[MOTH_RISK_IDX]], tags[requestlist[MOTH_TAG_IDX]],\
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


def assigningTimeAndDoctor(mothers, oldDoctors, oldSchedule):
    """
    
    """
    horasAssigned = None
    doctorAssigned = None
    motherAssigned = None

    headerRequests = saveHeader(mothers)
    headerOldDoctors = saveHeader(oldDoctors)
    headerOldSchedule = saveHeader(oldSchedule)

    newSchedule = []
    newScheduleList = []

    #part for redirecting to the other network (works great)
    for assignedTimeFromOldSchedule in readScheduleFile(oldSchedule):
        if hourToInt(updateHours(assignedTimeFromOldSchedule[0], 20)) >= 20:
            horasAssigned = REDIR_HOURS
            doctorAssigned = REDIR_STR
        else:
            print("good")

    #part for adding mothers from the old schedule if the time of the appointment 
    #is bigger than the time of the new schedule (works great)
    for appointment in readScheduleFile(oldSchedule):
        if hourToInt(appointment[0]) >= hourToInt(headerOldSchedule[HEADER_TIME_IDX][0])\
              and minutesToInt(appointment[0]) >= minutesToInt(headerOldSchedule[HEADER_TIME_IDX][0])+30:
            newScheduleList.append(appointment)


    #test part for making assigments. Started working somehow. Still pretty bad
    mothersList = readRequestsFile(mothers)
    doctorsList = readDoctorsFile(oldDoctors)

    sortedMothers = sorted(mothersList, key=sortRequests)
    sortedDoctors = sorted(doctorsList, key=sortDoctors)

    """for i in range(len(sortedMothers)):
        schedule = []
        for j in range(len(sortedDoctors)):
            if i == j:
                schedule.append(sortedDoctors[j][DOCT_BIRTH_END_IDX])
                schedule.append(sortedMothers[j][0])
                schedule.append(sortedDoctors[j][0])
            elif i > j:
                schedule.append(REDIR_HOURS)
                schedule.append(sortedMothers[j][0])
                schedule.append(REDIR_STR)
        newScheduleList.append(schedule)
    
    schedule = []
    for i in range(len(sortedMothers)):
        schedule.append(sortedMothers[i][0])
        schedule.append(sortedDoctors[i][0])
        newScheduleList.append(schedule)"""

    return newScheduleList

#print(assigningTimeAndDoctor("requests10h30.txt", "doctors10h00.txt", "schedule10h00.txt"))

def makeAssingment(mothers, oldDoctors):
    newScheduleList = []
    assignedDoctors = []

    mothersList = readRequestsFile(mothers)
    doctorsList = readDoctorsFile(oldDoctors)

    sortedMothers = sorted(mothersList, key=sortRequests)
    sortedDoctors = sorted(doctorsList, key=sortDoctors)

    for mother in sortedMothers:
        timeAssigned = None
        doctorAssigned = None
        isDoctorAssigned = False

        for doctor in sortedDoctors:
            if (
                (mother[MOTH_RISK_IDX] == "high" and int(doctor[DOCT_SKILL_IDX]) >= 2 and isDoctorAssigned == False)
                or (mother[MOTH_RISK_IDX] == "low" and int(doctor[DOCT_SKILL_IDX]) >= 1 and isDoctorAssigned == False)
            ) and doctor not in assignedDoctors:
                timeAssigned = doctor[DOCT_BIRTH_END_IDX]
                doctorAssigned = doctor[DOCT_NAME_IDX]
                appointment = [timeAssigned, mother[MOTH_NAME_IDX], doctorAssigned]
                newScheduleList.append(appointment)
                assignedDoctors.append(doctor)
                isDoctorAssigned = True
                break

        if not isDoctorAssigned:
            timeAssigned = REDIR_HOURS
            doctorAssigned = REDIR_STR
            appointment = [timeAssigned, mother[MOTH_NAME_IDX], doctorAssigned]
            newScheduleList.append(appointment)

    return newScheduleList

print(makeAssingment("requests16h30.txt", "doctors16h00.txt"))


"""doctors = readDoctorsFile("doctors10h00.txt")
doctors.sort(key=sortDoctors)

for doctor in doctors:
    print(doctor)"""
    
#or (mother[MOTH_RISK_IDX] == "low" and int(doctor[DOCT_SKILL_IDX]) >= 1)
##########################################################################
############################### TESTS ####################################
##########################################################################


def nothing():
    """highMoms = []
        lowMoms = []

        greenMoms = []
        yellowMoms = []
        redMoms = []

        highLevelDoctors = []

        for mother in readRequestsFile(mothers):
            if mother[MOTH_RISK_IDX] == "high":
                highMoms.append(mother[MOTH_NAME_IDX])
            elif mother[MOTH_RISK_IDX] == "low":
                lowMoms.append(mother[MOTH_NAME_IDX])

            if mother[MOTH_TAG_IDX] == "green":
                greenMoms.append(mother[MOTH_NAME_IDX])
            elif mother[MOTH_TAG_IDX] == "yellow":
                yellowMoms.append(mother[MOTH_NAME_IDX])
            elif mother[MOTH_TAG_IDX] == "red":
                redMoms.append(mother[MOTH_NAME_IDX])

        for doctor in readDoctorsFile(oldDoctors):
            if int(doctor[DOCT_SKILL_IDX]) >= 2:
                highLevelDoctors.append(doctor[DOCT_NAME_IDX])


                #horasAssigned = doctor[DOCT_BIRTH_END_IDX]
                #motherAssigned = mother[MOTH_NAME_IDX]
                #doctorAssigned = doctor[DOCT_NAME_IDX]"""
