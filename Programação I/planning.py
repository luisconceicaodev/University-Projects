#-*- coding: utf-8 -*-

# 2015-2016 Programacao 1 (LTI)
# Grupo 007
# 48303 Luís Miguel Duarte Conceição
# 48340 Chandani Tushar Narendra


from itertools import cycle
import operator
import copy
from consultStatus import *
from constants import *

from timeTT import hourToInt
from timeTT import minutesToInt
from timeTT import intToTime
from timeTT import add
from timeTT import diff


def updateServices(reservations_p, waiting4ServicesList_prevp):

    """Assigns drivers with their vehicles to services that were reserved.
    
    Requires:
    reservations_p is a list with a structure as in the output of
    consultStatus.readReservationsFile; waiting4ServicesList_prevp is a list
    with the structure as in the output of consultStatus.waiting4ServicesList;
    objects in reservations_p concern a period p, and objects in
    waiting4ServicesList_prevp concern a period immediately preceding p.
    Ensures:
    list L of lists, where each list has the structure of
    consultStatus.readServicesFile, representing the services to be provided
    in a period starting in the beginning of the period p upon they having
    been reserved as they are represented in reservations_p;
    Reservations with earlier booking times are served first (lexicographic
    order of clients' names is used to resolve eventual ties);
    Drivers available earlier are assigned services first (lexicographic
    order of their names is used to resolve eventual ties) under
    the following conditions:
    If a driver has less than 30 minutes left to reach their 5 hour
    daily limit of accumulated activity, he is given no further service
    in that day (this is represented with a service entry marhed with
    "terminates");
    Else if a vehicle has less than 15 kms autonomy, it is recharged
    (this is represented with a service entry marked with "charges") and
    is available 1 hour later, after recharging (this is represented with
    another service entry, marked with "standby").
    in this list L:
    drivers terminating their services earlier have priority over the ones
    terminating later;
    in case of eventual ties, drivers with less accumulated time have
    priority over the ones with more accumulated time;
    lexicographic order of drivers's names decides eventual ties
    in each case above.
    """
    
    available = waiting4ServicesList_prevp
    reservations = reservations_p 
    terminated = []
    charges = []
    cycle = 0

    for r in reservations:
        CircuitTime = diff(r[INDEXRequestedEndHour],r[INDEXRequestedStartHour])
        cycle = 0
        while cycle <= len(available)-1:
            if hourToInt(add(available[cycle][INDEXAccumulatedTime],CircuitTime)) != 05 and \
                         int(available[cycle][INDEXVehicAutonomy]) >= \
                         int(available[cycle][INDEXAccumulatedKms]) + int(r[INDEXCircuitKmsInReservation]):
                service = available.pop(cycle)
                
                service[INDEXClientName] = r[INDEXClientNameInReservation]
                service[INDEXClientName] = r[INDEXClientNameInReservation]
                service[INDEXDepartureHour] = r[INDEXRequestedStartHour]
                service[INDEXArrivalHour] = r[INDEXRequestedEndHour]
                service[INDEXCircuitId] = r[INDEXCircuitInReservation]
                service[INDEXCircuitKms] = r[INDEXCircuitKmsInReservation]
                service[INDEXAccumulatedKms] = int(service[INDEXAccumulatedKms]) + \
                                               int(r[INDEXCircuitKmsInReservation])
                hourToInt(service[INDEXAccumulatedTime])
                minutesToInt(service[INDEXAccumulatedTime])
                service[INDEXAccumulatedTime] = add(service[INDEXAccumulatedTime], \
                                               diff(r[INDEXRequestedEndHour],r[INDEXRequestedStartHour]))
                available.append(service)
                break
            else:
                cycle += 1
         
    for service in range(0, len(available)):
        if hourToInt(diff(TIMELimit,available[service][INDEXAccumulatedTime])) == 00 and \
           minutesToInt(diff(TIMELimit,available[service][INDEXAccumulatedTime])) <= 30:
            available[service][INDEXDriverStatus] = STATUSTerminated
            terminated.append(available[service])
            
        if (int(available[service][INDEXVehicAutonomy]) - 15 <= int(available[service][INDEXCircuitKms]) \
            + int(available[service][INDEXAccumulatedKms]) and (available[service] not in terminated)):
             available[service][INDEXDriverStatus] = STATUSCharging
             charges.append(available[service])
                
    available = sorted(available, key = operator.itemgetter(INDEXArrivalHour,\
                                                            INDEXAccumulatedTime, INDEXClientName))
    
    return available





    
