#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from constants import *
from dateTime import *
from planning import *
from infoFromFiles import *


#function for writing new schedule file
def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the mothers assigned;
    header is a list with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    outFileSchedule = open(fileName, "w", encoding="utf-8")     #opening the file for writing
    for headLine in header:                                     #searching through header
        outFileSchedule.write(' '.join(headLine) + '\n')        #writing the header line by line to the file
    for index, schedule in enumerate(sched):                    #searching through index and schedule in sched
        if index >= len(sched) - 1:                             #check if it's the last list in sched
            outFileSchedule.write(', '.join(schedule))          #if it's writing the file without the paragraph(i.e. "\n") at the end
        else:                                                   #check if it's not the last list in sched
            outFileSchedule.write(', '.join(schedule) + '\n')   #if it's not writing the file wit the paragraph(i.e. "\n") at the end

    outFileSchedule.close()                                     #closing the file, so the memory is free


#function for writing new doctors file
def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a collection of updated doctors into a file.

    Requires:
    doctors is a list with the structure as in the output of
    planning.updateDoctors representing the updated doctors;
    header is a list with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.

    Ensures:
    writing of file named fileName representing the updated doctors,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the updated doctors as ordered head to tail in doctors.
    """
    outFileDoctors = open(fileName, "w", encoding="utf-8")      #opening the file for writing
    for headLine in header:                                     #searching through header
        outFileDoctors.write(' '.join(headLine) + '\n')         #writing the header line by line to the file
    for index, doctor in enumerate(doctors):                    #searching through index and doctor in doctors
        if index >= len(doctors) - 1:                           #check if it's the last list in doctors
            outFileDoctors.write(', '.join(doctor))             #if it's writing the file without the paragraph(i.e. "\n") at the end
        else:                                                   #check if it's not the last list in doctors
            outFileDoctors.write(', '.join(doctor) + '\n')      #if it's not writing the file wit the paragraph(i.e. "\n") at the end

    outFileDoctors.close()                                      #closing the file, so the memory is free