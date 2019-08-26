#-*- coding: utf-8 -*-

# 2015-2016 Programacao 1 (LTI)
# Grupo 007
# 48303 Luís Miguel Duarte Conceição
# 48340 Chandani Tushar Narendra



def hourToInt(time):
    """
    Converts hour from string to integer.
    Requires:
    time is string with the following format: hour:minutes example 00:00.
    Ensures:
    hour value from time is converted to integer.
    """
    t = time.split(":")
    return int(t[0])



def minutesToInt(time):
    """
    Converts minutes from string to integer.
    Requires:
    time is string with the following format: hour:minutes, example 00:00.
    Ensures:
    minutes value from time is converted to integer.
    """
    t = time.split(":")
    return int(t[1])



def intToTime(hour, minutes):
    """
    Converts hour and minutes values from string to integer with
    the following format: hour:minutes
    Requires:
    hour and minutes values
    Ensures:
    hour and minutes are converted to string with the
    following format: hour:minutes
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m



def add(time1, time2):
    """
    Adds time1 and time2
    Requires:
    time1 and time2 are strings with the following
    format hour:minutes example 00:00
    Ensures:
    time1 and time2 are added and returned in the
    following format hour:minutes example 00:00
    """
    t1Hour = hourToInt(time1)
    t1Minutes = minutesToInt(time1)
    t2Hour = hourToInt(time2)
    t2Minutes = minutesToInt(time2)

    hours = (t1Minutes + t2Minutes) / 60
    minutes = (t1Minutes + t2Minutes) % 60

    t1H = t1Hour + t2Hour + hours
    t1M = minutes

    return intToTime(t1H, t1M)



def diff(time1, time2):
    """
    Returns the difference in time between time1 and time2
    Requires:
    time1 and time2 are strings with the following
    format hour:minutes example 00:00
    Ensures:
    returns the difference in time between time1 and time2
    with the following format hour:minutes example 00:00
    """
    t1Hour = hourToInt(time1)
    t1Minutes = minutesToInt(time1)
    t2Hour = hourToInt(time2)
    t2Minutes = minutesToInt(time2)

    t1H = t1Hour - t2Hour
    minutes = t1Minutes - t2Minutes
    t1M = abs(minutes)

    if minutes < 0:
        t1H = t1H - 1
        t1M = 60 - t1M
        
    if t1H < 0:
        t1H = 0
        t1M = 0

    return intToTime(t1H, t1M)


