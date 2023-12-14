from constants import *
from testAddingTimes import *
from infoFromFiles import *

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


    return newScheduleList#, highMoms, highLevelDoctors, lowMoms, greenMoms, yellowMoms, redMoms

print(assigningTimeAndDoctor("requests10h30.txt", "doctors10h00.txt", "schedule10h00.txt"))


def sortRequests(requestlist):
	"""
     
	"""
	risks={"high":1, "low":2}
	tags={"red": 3, "yellow":2, "green":1}
	return (risks[requestlist[MOTH_RISK_IDX]], tags[requestlist[MOTH_TAG_IDX]],\
          -int(requestlist[MOTH_AGE_IDX]), requestlist[MOTH_NAME_IDX])



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