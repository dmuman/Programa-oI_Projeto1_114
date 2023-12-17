# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from constants import *
from dateTime import *


def removeHeader(fileName):
    """
    Skips the given amount of lines(NUM_HEADER_LINES) in a given file(i.e. header)

    Requires: fileName is already opened file, header is presented inside the file.
    Ensures: that the given number of lines are skipped when reading the .txt file.
    """

    for _ in range(NUM_HEADER_LINES):
        fileName.readline()

    return fileName


def saveHeader(fileName):
    """
    Saves the header into a list, containing lists, each of one has the line of the header, corresponding to the index.

    Requires: fileName is a str with the ending of a .txt, header is presented inside the file.
    Ensures: that the given number of lines(NUM_HEADER_LINES) are saved into a list when reading the .txt file(i.e. header)
    """
    inFile = open(fileName, "r", encoding = "utf-8")

    header = []
    headertemp = []
    headerData = []
    for _ in range(NUM_HEADER_LINES):
        headerData = inFile.readline()
        headertemp.append(headerData)
    
    for line in headertemp:
        headertemp = line.rstrip().split(", ")
        header.append(headertemp)

    return header


def timeAndDataFromHeader(fileName):
    """
    Receives the str fileName with the .txt at the end, end then returns the list, 
    containing time and data presented in the header. Header is given from the saveHeader() function.

    Requires: fileName is a string with the .txt at the end. Header is presented inside the file.
    Ensures: list, containing two lists that each has the corresponding time and data that are presented in the header.
    """
    timeList = saveHeader(fileName)[HEADER_TIME_IDX]
    dateList = saveHeader(fileName)[HEADER_DATE_IDX]
    
    return [timeList, dateList]


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
    try:
        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))       

        timeInName = fileName[-9:-4]
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]

        if saveHeader(fileName)[6][0] != "Doctors:":
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")
        elif timeInName != timeInHeader:
            raise IOError("time in the header and in the name are not the same")
        else:
            doctorsList = [] 
            for line in inFile:
                doctorsData = line.rstrip().split(", ")
                if len(doctorsData) != 1:
                    doctorsList.append(doctorsData)

        return doctorsList
    
    except IOError as e:
        print(f"File head error: {e}")


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into 
    a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that request),
    following the order provided in the lines of the file.
    """
    try:

        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))       

        timeInName = fileName[-9:-4]
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]

        if saveHeader(fileName)[6][0] != "Mothers:":
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")
        elif timeInName != timeInHeader:
            raise IOError("time in the header and in the name are not the same")
        else:
            requestsList = [] 
            for line in inFile:
                requestData = line.rstrip().split(", ")
                if len(requestData) != 1:
                    requestsList.append(requestData)        

        return requestsList
    
    except IOError as e:
        print(f"File head error: {e}")


def readScheduleFile(fileName):
    """
    Reads a file with an existing list of schedule with a given file name into 
    a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of schedules organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a schedule listed in
    the file fileName (with all the info pieces belonging to that schedule),
    following the order provided in the lines of the file.
    """
    try:
        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))      

        timeInName = fileName[-9:-4]
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]

        if saveHeader(fileName)[6][0] != "Schedule:":
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")
        elif timeInName != timeInHeader:
            raise IOError("time in the header and in the name are not the same")
        else: 
            scheduleList = [] 
            for line in inFile:
                scheduleData = line.rstrip().split(", ")
                if len(scheduleData) != 1:
                    scheduleList.append(scheduleData)        

        return scheduleList
    
    except IOError as e:
        print(f"File head error: {e}")
