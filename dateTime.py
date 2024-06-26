#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha


#function for transforming string hours to int
def hourToInt(time):
    """
    Gets the provided time in type string that has the letter 'h' inside of it 
    that separates hours and minutes and then returns the amount of hours in type int.

    Requires: time is a string and has the letter 'h' inside that separates hours and minutes.
    Ensures: the amount of hours in the type of int, that is provided 
    before the letter 'h' inside of the provided time.
    Examples:
    >>> hourToInt("14h00")
    14
    >>> hourToInt("09h30")
    9
    """
    t = time.split("h")     #splitting the time by the letter "h"
    hours = int(t[0])       #getting hours

    return hours


#function for transforming string minutes to int
def minutesToInt(time):
    """
    Gets the provided time in type string that has the letter 'h' inside of it 
    that separates hours and minutes and then returns the amount of minutes in type int.

    Requires: time is a string and has the letter 'h' inside that separates hours and minutes.
    Ensures: the amount of minutes in the type of int, that is provided 
    after the letter 'h' inside of the provided time.
    Examples:
    >>> minutesToInt("14h00")
    0
    >>> minutesToInt("09h30")
    30
    """
    t = time.split("h")     #splitting the time by the letter "h"
    minutes = int(t[1])     #getting the minutes

    return minutes


#function for transforming string day to int
def dayToInt(data):
    """
    Gets the provided data in type string that has the two dots sigh ':' inside of it 
    that separates day, month and year and then returns the day in type int.

    Requires: data is a string and has the two dots sign ':' inside that separates day, month and year.
    Ensures: the day in the type of int, that is provided before the first occurance 
    of the two dots sign ':' inside of the provided data.
    Examples:
    >>> dayToInt("21:12:2023")
    21
    >>> dayToInt("01:10:2023")
    1
    """
    t = data.split(":")     #splitting the date by the two dots sign ":"
    day = int(t[0])         #getting the day

    return day


#function for transforming string month to int
def monthToInt(data):
    """
    Gets the provided data in type string that has the two dots sigh ':' inside of it 
    that separates day, month and year and then returns the month in type int.

    Requires: data is a string and has the two dots sign ':' inside that separates day, month and year.
    Ensures: the month in the type of int, that is provided between the first and the second occurance 
    of the two dots sign ':' inside of the provided data.
    >>> monthToInt("21:12:2023")
    12
    >>> monthToInt("01:05:2023")
    5
    """
    t = data.split(":")     #splitting the date by the two dots sign ":"
    month = int(t[1])       #getting the month

    return month


#function for transforming string year to int
def yearToInt(data):
    """
    Gets the provided data in type string that has the two dots sigh ':' inside of it 
    that separates day, month and year and then returns the year in type int.

    Requires: data is a string and has the two dots sign ':' inside that separates day, month and year.
    Ensures: the year in the type of int, that is provided after the second occurance 
    of the two dots sign ':' inside of the provided data.
    >>> yearToInt("21:12:2023")
    2023
    >>> yearToInt("21:12:0023")
    23
    """
    t = data.split(":")     #splitting the date by the two dots sign ":"
    year = int(t[2])        #getting the year

    return year


#function for transforming int hours and minutes to string time
def intToTime(hour, minutes):
    """
    Gets the provided amount of hours and minutes, separated by commas, in the type of int 
    and returns the time of type string with the look of 'hourshminutes'. 
    Hours and minutes are separated by the letter 'h'.

    Requires: hour and minutes are positive integers, hour is less than 24 and minutes is less than 60.
    Ensures: string representation of the provided amount of hours and minutes, separated by the letter 'h'.
    >>> intToTime(9, 0)
    '09h00'
    >>> intToTime(14, 30)
    '14h30'
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h         #adding zero at the beginning to the hours, if hours are less then 10. 9 become "09", for example

    if minutes < 10 or minutes == 0:
        m = "0" + m         #adding zero at the beginning to the minutes, if minutes are less then 10. 0 become "00", for example

    time = f"{h}h{m}"       #creating a new string for the time

    return time


#function for transforming int day, month and year to string date
def intToData(day, month, year):
    """
    Gets the provided day, month and year, separated by commas, in the type of int 
    and returns the data of type string with the look of 'day:month:year'.
    Day, month and year are separated by the two dots sign ':'.

    Requires: day, month and year are positive integers, day is less than 32, 
    month is less than 13 and year is equal to the current year(2023).
    Ensures: string representation of the provided day, month and year, separated by the two dots sign ':'.
    >>> intToData(8, 1, 2023)
    '08:01:2023'
    >>> intToData(21, 12, 2023)
    '21:12:2023'
    """
    d = str(day)
    m = str(month)
    y = str(year)

    if day < 10:
        d = "0" + d         #adding zero at the beginning to the day, if day is less then 10. 6 become "06", for example

    if month < 10:
        m = "0" + m         #adding zero at the beginning to the month, if month is less then 10. 1 become "01", for example

    data = f"{d}:{m}:{y}"   #creating a new string for the data

    return data


#function for updating string time with int minutes
def updateHours(hoursToUpdate, minutesToAdd):
    """
    Updates the time with the given time to update and minutes to add. 
    Time is in the format of HHhMM, minutesToAdd are integers.
    Using converting time functions to get the hours and minutes and then to update those.
    It has three cases:
    If the added minutes ultrapassed 60(i.e. more than one hour)
    If the added minutes is iqual 60(i.e. iqual one hour)
    If the added minutes are less than 60(i.e. less than one hour)

    Requires: hoursToUpdate is a string in the format of HHhMM, minutesToAdd is integer

    Ensures: new, updated time with the given amount of minutes, in type string in the format of HHhMM

    >>> updateHours("14h25", 40)
    '15h05'
    >>> updateHours("14h25", 35)
    '15h00'
    >>> updateHours("14h25", 30)
    '14h55'
    >>> updateHours("23h30", 40)
    '00h10'
    """
    #declaring variables for holding the int representatin of hours, minutes and total minutes
    intHours = None 
    intMinutes = None
    totalMinutes = None

    #declaring variable for the new, updated hours
    updatedHours = None

    #in case new minutes are greater than 60
    if minutesToInt(hoursToUpdate) + minutesToAdd > 60:
        intHours = hourToInt(hoursToUpdate)                                 #assigning hours
        intMinutes = minutesToInt(hoursToUpdate)                            #assigning minutes
        totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
        updatedHours = intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes

    #in case new minutes are equal 60
    elif minutesToInt(hoursToUpdate) + minutesToAdd == 60:
        intHours = hourToInt(hoursToUpdate) + 1         #updating hours(adding 1 hour)
        intMinutes = 0                                  #updating minutes(equal 00)
        updatedHours = intToTime(intHours, intMinutes)  #new, updated hours

    #in case new minutes are less than 60
    else:
        intHours = hourToInt(hoursToUpdate)                     #assigning hours. they remain the same
        intMinutes = minutesToInt(hoursToUpdate) + minutesToAdd #updating minutes with minutesToAdd
        updatedHours = intToTime(intHours, intMinutes)          #new, updated hours

    return updatedHours

#testing part
if __name__ == "__main__":
    import doctest
    doctest.testmod()