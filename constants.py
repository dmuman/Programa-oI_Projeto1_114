#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 114
# 59348 Dmytro Umanskyi 
# 62263 Eduardo Rocha



# This module records the constants used in the application

# You should define here as many constants as you need to keep your 
# code clean and legible



# Value for weekly pause in the output schedule
WKL_PAUSE = "weekly leave"

# Value for redirected string and hours
REDIR_HOURS = "HHhMM"
REDIR_STR = "redirected to other network"

# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7


# In a doctor's list:
# Index of the element with the doctor's name
DOCT_NAME_IDX = 0
# Index of the element with the doctor's professional experience:
DOCT_SKILL_IDX = 1
# Index of the element with the planned time the childbirth assistance ends:
DOCT_BIRTH_END_IDX = 2
# Index of the element with the minutes accumulated since the beginning of the day:
DOCT_DAILY_HOURS_IDX = 3
# Index of the element with the hours and minutes accumulated since the last weekly rest:
DOCT_REST_HOURS_IDX = 4

# In a mother's list:
# Index of the element with the mother's name:
MOTH_NAME_IDX = 0
# Index of the element with the mother's age:
MOTH_AGE_IDX = 1
# Index of the element with the mother's tag colour:
MOTH_TAG_IDX = 2
# Index of the element with the childbirth risk:
MOTH_RISK_IDX = 3

# In a header
# Index of the element with the header's time
HEADER_TIME_IDX = 3
# Index of the element with the header's date
HEADER_DATE_IDX = 5