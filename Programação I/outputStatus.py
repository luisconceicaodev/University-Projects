#-*- coding: utf-8 -*-

# 2015-2016 Programacao 1 (LTI)
# Grupo 007
# 48303 Luís Miguel Duarte Conceição
# 48340 Chandani Tushar Narendra

from planning import updateServices
from constants import NUMBEROfLinesInHeader
from constants import INDEXAccumulatedTime
from consultStatus import *

def header_p(file_name):
    """Reads the first 7 lines of a .txt file with a list of reservations.

    Requires:
    file_name is a .txt file with a list of reservations for the next period
    Ensures:
    String with a header concerning period p
    """
    
    h = ""
    inFile = open(file_name,'r')
    for line in range(0, NUMBEROfLinesInHeader):
        h += str(inFile.readline())
    inFile.close()
    
    return h


def writeServicesFile(services_p, file_name_p, header_p):
    """Writes a collection of services into a file.

    Requires:
    services_p is a list with the structure as in the output of
    updateServices representing the services in a period p;
    file_name_p is a str with the name of a .txt file whose end (before
    the .txt suffix) indicates the period p, as in the examples provided in
    the general specification (omitted here for the sake of readability);
    and header is a string with a header concerning period p, as in
    the examples provided in the general specification (omitted here for
    the sake of readability).
    Ensures:
    writing of file named file_name_p representing the collection of
    services in services_p and organized as in the examples provided in
    the general specification (omitted here for the sake of readability);
    in the listing in this file keep the ordering of services in services_p.
    """
    
    output = open(file_name_p,'w')
    output.write(header_p)
    for item in services_p:
        output.write(str(item[:INDEXAccumulatedTime]).replace(']','')\
                     .replace('[','').replace("'", ''))
        output.write('\n')
    
    output.close()
    
    return output
