# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha

from constants import *
from dateTime import *


#function for skipping the header in the given file
def removeHeader(fileName):
    """
    Skips the given amount of lines(NUM_HEADER_LINES) 
    in a given file(i.e. header)

    Requires: fileName is already opened file, 
    header is presented inside the file.

    Ensures: that the given number of lines 
    are skipped when reading the .txt file.
    """

    for _ in range(NUM_HEADER_LINES): #using placeholder that skips the given amount of lines
        fileName.readline()

    return fileName


#function for saving the header from the given file
def saveHeader(fileName):
    """
    Saves the header into a list, containing lists, 
    each of one has the line of the header, corresponding to the index.

    Requires: fileName is a str with the ending of a .txt, 
    header is presented inside the file.

    Ensures: that the given number of lines(NUM_HEADER_LINES) 
    are saved into a list when reading the .txt file(i.e. header)
    """
    inFile = open(fileName, "r", encoding = "utf-8") #opening the file

    #declaring variables for the header, temporary header and it's data
    header = []
    headertemp = []
    headerData = []

    for _ in range(NUM_HEADER_LINES):               #using placeholder do write to the header only given amount of lines
        headerData = inFile.readline()              #headerData is equal to each line in header
        headertemp.append(headerData)               #appending temporary header with headerData
    
    for line in headertemp:                         #searching through the temporary header
        headertemp = line.rstrip().split(", ")      #splitting the info by commas
        header.append(headertemp)                   #appending the header

    return header


#function for getting time and date from the header
def timeAndDataFromHeader(fileName):
    """
    Receives the str fileName with the .txt at the end, 
    and then returns the list, containing time and data presented in the header. 
    Header is given from the saveHeader() function.

    Requires: fileName is a string with the .txt at the end. 
    Header is presented inside the file.

    Ensures: list, containing two lists that each has the 
    corresponding time and data that are presented in the header.
    """
    timeList = saveHeader(fileName)[HEADER_TIME_IDX] #gaining the time from the given header on the given index
    dateList = saveHeader(fileName)[HEADER_DATE_IDX] #gaining the data from the given header on the given index
    
    return [timeList, dateList]                      #returning the list, that contains lists of time and data


#function for reading the doctors file
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
        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))          #opening the file with removed header

        timeInName = fileName[-9:-4]                                            #getting time from the fileName
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]                    #getting time from the header

        if saveHeader(fileName)[6][0] != "Doctors:":                            #checking if the name of the file and inside the header are correct 
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")  #raising an error if not
        elif timeInName != timeInHeader:                                        #checking if the time in the fileNmae and inside the header are the same 
            raise IOError("time in the header and in the name are not the same")                #raising an error if not
        else:                                                                   #if there're no errors
            doctorsList = []                                                    #declaring variable for the doctors list
            for line in inFile:
                doctorsData = line.rstrip().split(", ")                         #splitting the info
                if len(doctorsData) != 1:                                       #check if the lengh of the data is greater than 1
                    doctorsList.append(doctorsData)                             #appending doctors list

        return doctorsList
    
    except IOError as e:
        print(f"File head error: {e}")                                          #printing an error if it's raised


#function for reading the requests file
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

        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))          #opening the file with removed header

        timeInName = fileName[-9:-4]                                            #getting time from the fileName
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]                    #getting time from the header

        if saveHeader(fileName)[6][0] != "Mothers:":                            #checking if the name of the file and inside the header are correct
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")  #raising an error if not
        elif timeInName != timeInHeader:                                        #checking if the time in the fileNmae and inside the header are the same
            raise IOError("time in the header and in the name are not the same")                #raising an error if not
        else:                                                                   #if there're no errors
            requestsList = []                                                   #declaring variable for the requests list
            for line in inFile:
                requestData = line.rstrip().split(", ")                         #splitting the info
                if len(requestData) != 1:                                       #check if the lengh of the data is greater than 1
                    requestsList.append(requestData)                            #appending requests list

        return requestsList
    
    except IOError as e:
        print(f"File head error: {e}")                                          #printing an error if it's raised


#function for reading the schedule file
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
        inFile = removeHeader(open(fileName, "r", encoding = "utf-8"))          #opening the file with removed header

        timeInName = fileName[-9:-4]                                            #getting time from the fileName
        timeInHeader = timeAndDataFromHeader(fileName)[0][0]                    #getting time from the header

        if saveHeader(fileName)[6][0] != "Schedule:":                           #checking if the name of the file and inside the header are correct
            raise IOError(f"scope inconsistency between name and header in file <{fileName}>")  #raising an error if not
        elif timeInName != timeInHeader:                                        #checking if the time in the fileNmae and inside the header are the same
            raise IOError("time in the header and in the name are not the same")                #raising an error if not
        else:                                                                   #if there're no errors
            scheduleList = []                                                   #declaring variable for the schedule list
            for line in inFile:
                scheduleData = line.rstrip().split(", ")                        #splitting the info
                if len(scheduleData) != 1:                                      #check if the lengh of the data is greater than 1
                    scheduleList.append(scheduleData)                           #appending requests list

        return scheduleList
    
    except IOError as e:
        print(f"File head error: {e}")                                          #printing an error if it's raised
