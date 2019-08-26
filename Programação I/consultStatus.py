#-*- coding: utf-8 -*-

# 2015-2016 Programacao 1 (LTI)
# Grupo 007
# 48303 Luís Miguel Duarte Conceição
# 48340 Chandani Tushar Narendra

import operator
import copy
from constants import INDEXDriverName
from constants import NUMBEROfLinesInHeader
from constants import INDEXVehiclePlateInDict
from constants import INDEXArrivalHour
from constants import INDEXRequestedStartHour
from constants import STATUSTerminated
from constants import STATUSCharging
from constants import INDEXClientNameInReservation
from constants import STATUSCharging
from constants import STATUSStandBy
from constants import INDEXDriverStatus
from constants import INDEXClientName
from constants import INDEXCircuitId
from constants import INDEXCircuitKms
from constants import NOCIRCUIT
from constants import NOCLIENT
from constants import INDEXAccumulatedTime
from constants import INDEXVehiclePlate
from constants import INDEXAccumulatedTimeInDict
from constants import INDEXVehicleAutonomyInDict

def readDriversFile(file_name):
    """Reads a file with a list of drivers into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of drivers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a driver listed in
    file with name file_name, a key is the string with the name of a driver,
    and a value is the list with the other elements belonging to that
    driver, in the order provided in the lines of the file.
    """

    inFile = open(file_name, "r")
    inFile = inFile.readlines()[NUMBEROfLinesInHeader:]
    driversDict = {}
    for line in inFile:
        driverData = line.rstrip().split(", ")
        driverName = driverData.pop(INDEXDriverName)
        driversDict[driverName] = driverData
    
    return driversDict


def readVehiclesFile(file_name):
    """Reads a file with a list of vehicles into a collection.

    Requires:
    .txt file with information on vehicle license plates, maximum battery
    autonomy and the amount of battery used since the last charge.
    Ensues:
    dict where each key corresponds to a vehicle license plate with each
    respectively value being a list with its maximum battery autonomy
    and amount of battery used since the last charge.
    
    """

    inFile = open(file_name, "r")
    inFile = inFile.readlines()[NUMBEROfLinesInHeader:]
    vehiclesDict = {} 
    for line in inFile:
        vehicleData = line.rstrip().split(", ")
        vehiclePlate = vehicleData.pop(INDEXVehiclePlateInDict)
        vehiclesDict[vehiclePlate] = vehicleData        
    
    return vehiclesDict



def readServicesFile(file_name):
    """Reads a file with a list of services into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of services organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list L of lists, where each list corresponds to a service listed
    in file with name file_name and its elements are the elements
    belonging to that service in the order provided in the lines of
    the file.
    in this list L:
    drivers terminating their services earlier have priority over the ones
    terminating later;
    lexicographic order of drivers's names decides eventual ties
    in each case above.
    """
    
    inFile = open(file_name, "r")       
    inFile = inFile.readlines()[NUMBEROfLinesInHeader:]
    servicesList = [] 
    for line in inFile:
        servicesList.append(line.rstrip().split(", "))
    servicesList = sorted(servicesList, \
                          key=operator.itemgetter(INDEXArrivalHour, \
                                                  INDEXDriverName))
    
    return servicesList



def readReservationsFile(file_name):
    """Reads a file with a list of reservations into a collection.

    Requires:
    file_name is a string with the name of a .txt file containing
    a list of reservations organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list L of lists, where each list corresponds to a reservation
    listed in file name with file_name and its elements are
    the elements belonging to that reservation in the order provided in
    the lines of the file.
    in this list L:
    clients reserving a service with an earlier starting time have
    priority over the ones with later starting times;
    lexicographic order of clients's names decides eventual ties.
    """

    inFile = open(file_name,"r")
    inFile = inFile.readlines()[NUMBEROfLinesInHeader:]
    reservationsList = []
    for line in inFile:
        reservationsList.append(line.rstrip().split(", "))
    reservationsList = sorted(reservationsList, \
                              key=operator.itemgetter(INDEXRequestedStartHour, \
                                                      INDEXClientNameInReservation))
    
    return reservationsList

def resetVehic(file_name):
    """
    Creates a list L of lists with updates info for drivers that need
    to charge their vehicles.
    
    Requires:
    list L of lists with a structure similar to the output of
    readServicesFile.
    Ensures:
    a list L of lists with a structure similar to the output of
    readServicesFile and obtained by checking if any list of lists
    has the string 'charges'. If any of them do it will do the following:
    - Add one more hour ("01:00") to the arrival hour;
    - Change the circuit assigned to "_no_circuit_";
    - Change the client name to "_no_client_";
    - Changes the circuit kms to '0'.
    """
    
    services = copy.deepcopy(readServicesFile(file_name))
    reset=[]
    for i in range(len(services)):
        services[i][INDEXDriverStatus] = STATUSStandBy
        services[i][INDEXCircuitId] = NOCIRCUIT
        services[i][INDEXClientName] = NOCLIENT
        services[i][INDEXCircuitKms] = '0'
        hourToInt(services[i][INDEXArrivalHour])
        minutesToInt(services[i][INDEXArrivalHour])
        services[i][INDEXArrivalHour] = add(services[i][INDEXArrivalHour],'01:00')
        reset.append(services[i])
    return reset

def waiting4ServicesList(drivers_p, vehicles_p, services_p):
    """Organizes a list of active drivers with their assigned
    vehicles that can take further services.

    Requires:
    drivers_p is a dict with a structure as in the output
    of readDriversFile; vehicles_p is a dict with the structure as in
    the output of readVehiclesFile; services_p is a list with the structure
    as in the output of readServicesFile; the objects in drivers_p,
    vehicles_p and services_p concern the same period p.
    Ensures:
    a list L of lists with a structure similar to the output of
    readServicesFile and obtained by:
    extracting the sublist SL of services_p where each list in
    that sublist SL corresponds to the last representation of an active
    driver, converted to a “standby” status (older representations of active
    drivers and representations of terminated drivers are excluded), 
 
    and by appending to each list of that subset SL 3 further elements:
    one with the accumulated time of the driver, another with the autonomy
    of his vehicle in kilometers for a fully charged batery, and yet
    another with the accumulated kilometers of that vehicle;
    in this list L:
    drivers terminating their services earlier have priority over the ones
    terminating later;
    in case of eventual ties, drivers with less accumulated time have
    priority over the ones with more accumulated time;
    lexicographic order of drivers's names decides eventual ties
    in each case above.
    """
    
    serviceList = copy.deepcopy(services_p)
    serviceList.reverse()

    driversInWaitingList = []
    detailedWaitingList = []

    # Obtains sublist SL
    for service in serviceList:
        driver = service[INDEXDriverName]
        driverTerminated = service[INDEXDriverStatus] == STATUSTerminated
        if (driver not in driversInWaitingList) and (not driverTerminated):
            #DEPRECATED: service = resetVehic(service, mode="standby")
            if service[INDEXDriverStatus] == STATUSCharging:    #REPLACEMENT
                service = resetVehic(service)                   #REPLACEMENT
            driversInWaitingList.append(driver)
            detailedWaitingList.append(service)

    # Enriches SL with 3 further data items
    for service in detailedWaitingList:
        driverName = service[INDEXDriverName]
        driverAccumulatedTime = drivers_p[driverName][INDEXAccumulatedTimeInDict]
        service.append(driverAccumulatedTime)
        vehiclePlate = service[INDEXVehiclePlate]
        vehicleKms = vehicles_p[vehiclePlate][INDEXVehicleAutonomyInDict:]
        service.extend(vehicleKms)
        
    # Puts it back to the original order
    detailedWaitingList.reverse()

    # Sorting according to increasing availability time,
    # untying with drivers's names
    detailedWaitingList = sorted(detailedWaitingList, \
                                 key=operator.itemgetter(INDEXArrivalHour, \
                                                INDEXAccumulatedTime, \
                                                INDEXDriverName))
    
    return detailedWaitingList


