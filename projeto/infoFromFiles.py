#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from constants import *


def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors with a given file name into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(open(fileName, "r"))       

    doctorsList = [] 
    for line in inFile:
        doctorsData = line.rstrip().split(", ")
        doctorsList.append(doctorsData)        

    return doctorsList



def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that request),
    following the order provided in the lines of the file.
    """

    inFile = removeHeader(open(fileName, "r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


def readScheduleFile(fileName):
    """
    Reads a file with an existing list of schedule with a given file name into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of schedules organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a schedule listed in
    the file fileName (with all the info pieces belonging to that schedule),
    following the order provided in the lines of the file.
    """

    inFile = removeHeader(open(fileName, "r"))       

    scheduleList = [] 
    for line in inFile:
        scheduleData = line.rstrip().split(", ")
        scheduleList.append(scheduleData)        

    return scheduleList

def removeHeader(file):

    for _ in range(NUM_HEADER_LINES):
        file.readline()
    return file

def saveHeader(file):

    inFile = open(file, "r")

    header = []
    for _ in range(NUM_HEADER_LINES):
        headerData = inFile.readline()
        header.append(headerData)
    #header = [inFile.readline() for _ in range(7)]

    return header

def timeAndDataFromHeader(file):

    inFile = saveHeader(file, "r")

    time = []

    data = []


#print(readScheduleFile("schedule10h00.txt"))
print(saveHeader("schedule10h00.txt"))

