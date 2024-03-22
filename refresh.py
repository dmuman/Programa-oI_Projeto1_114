#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from sys import argv
from infoFromFiles import *
from dateTime import *
from planning import *
from infoToFiles import *

#declaring variables for the file's name of doctors, schedule and requests using argv from the module sys
doctorsFileName = argv[1]
scheduleFileName = argv[2]
requestsFileName = argv[3]
    

#main fuction, that runs the program
def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of mothers requested at date d and time t+30mins;
    
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """

    try:
        #declaring variables for the headers from old doctors and schedule
        doctorsHeader = saveHeader(doctorsFileName)
        scheduleHeader = saveHeader(scheduleFileName)

        #updating the time in the headers by 30 minutes
        scheduleHeader[HEADER_TIME_IDX][0] = updateHours(scheduleHeader[HEADER_TIME_IDX][0], 30)
        doctorsHeader[HEADER_TIME_IDX][0] = updateHours(doctorsHeader[HEADER_TIME_IDX][0], 30)

        #declaring variables for the new schedule and new doctors, using update functions from the planning module
        newSchedule = updateSchedule(doctorsFileName, requestsFileName, scheduleFileName, scheduleHeader[HEADER_TIME_IDX][0])
        newDoctors = updateDoctors(doctorsFileName)

        #declaring variables for new names of the output files
        newScheduleFileName = f"schedule{scheduleHeader[HEADER_TIME_IDX][0]}.txt"   #adding the proper time in the name from the updated header
        newDoctorsFileName = f"doctors{doctorsHeader[HEADER_TIME_IDX][0]}.txt"      #adding the proper time in the name from the updated header
        
        #writing new files, using writing functions from the infoToFiles module
        writeScheduleFile(newSchedule, scheduleHeader, newScheduleFileName)
        writeDoctorsFile(newDoctors, doctorsHeader, newDoctorsFileName)

    except Exception:       #cathing and exception
        print("", end="")   #and ignoring it(i.e. printing exception only from the infoFromFiles module)


plan(doctorsFileName, scheduleFileName, requestsFileName) #executing the function(i.e. the whole program)