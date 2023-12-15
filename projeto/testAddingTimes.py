from dateTime import *
from constants import *

def updateDoctorsTime(oldFreeHours, oldMinutesDias, oldHorasSemanais, minutesToAdd):
    """
    
    """
    newFreeHours = None
    newHorasSemanais = None
    newMinutesDias = oldMinutesDias + minutesToAdd
    
    if newMinutesDias >= 240:
        newFreeHours = intToTime(hourToInt(oldFreeHours) + 1, minutesToInt(oldFreeHours))
    else:
        newFreeHours = updateHours(oldFreeHours, minutesToAdd)
    
    newHorasSemanais = updateHours(oldHorasSemanais, minutesToAdd)

    if hourToInt(newHorasSemanais) >= 40:
        newFreeHours = WKL_PAUSE

    return newFreeHours, newMinutesDias, newHorasSemanais

####################################################################
############################ TESTS #################################
####################################################################
#print(updateDoctorsTime("14h25", 100, "35h40", 45))
#print(updateDoctorsTime("14h25", 200, "35h40", 45))
#print(updateDoctorsTime("14h25", 100, "39h40", 45))
#print(updateDoctorsTime("14h25", 200, "39h40", 45))
#print(updateHours("9h50", 20))
