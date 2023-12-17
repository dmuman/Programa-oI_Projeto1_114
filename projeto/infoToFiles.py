#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from constants import *
from dateTime import *
from planning import *
from infoFromFiles import *

def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    #header[HEADER_TIME_IDX][0] = updateHours(header[HEADER_TIME_IDX][0], 30)
    #fileName = f"schedule{header[HEADER_TIME_IDX][0]}.txt"
    outFileSchedule = open(fileName, "w", encoding="utf-8")
    for headLine in header:
        outFileSchedule.write(' '.join(headLine) + '\n')
    for index, schedule in enumerate(sched):
        if index >= len(sched) - 1:
            outFileSchedule.write(', '.join(schedule))
        else:
            outFileSchedule.write(', '.join(schedule) + '\n')

    outFileSchedule.close()


def writeDoctorsFile(doctors, header, fileName):
    """
    
    """
    outFileDoctors = open(fileName, "w", encoding="utf-8")
    for headLine in header:
        outFileDoctors.write(' '.join(headLine) + '\n')
    for index, doctor in enumerate(doctors):
        if index >= len(doctors) - 1:
            outFileDoctors.write(', '.join(doctor))
        else:
            outFileDoctors.write(', '.join(doctor) + '\n')

    outFileDoctors.close()
