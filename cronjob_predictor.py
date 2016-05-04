__author__ = 'Olari Pipenberg'

import subprocess
import re
from croniter import croniter
from datetime import datetime

#Todo time scheduling

#Todo arguments, users, entry print

def getCronTable(): #read crontab output into variable
    cronTable = subprocess.check_output('crontab -l', shell=True)
    return cronTable

def getCronEntries(): #append crontab entry lines into list
    cronTable = getCronTable()
    lines = []
    for line in cronTable.splitlines():
        line = line.lstrip() #remove leading whitespaces
        if validateCronEntry(line) == True:
            lines.append(line)
    return lines

def validateCronEntry(cronLine): #validate correct crontab entry
    if not cronLine.strip(): #check for empty lines
        return False
    if cronLine.startswith("#"): #check if it is not comment
        return False
    if cronLine.startswith("@"): #check if it is special string
        print("Crontab entry contains special strings. Sorry they are not supported yet :(") #TODO?
        quit()
    return True

def timeLeft(arg):
    diff = arg-datetime.now()
    #Todo formating
    return diff.seconds

def getTime(cronFormat):
    base=datetime.now() #get current system time
    #print "Current time:",base
    iter = croniter(cronFormat, base)
    #TODO error handling, time global var?
    aeg = iter.get_next(datetime)
    print aeg
    #Todo next
    return aeg

def syntaxToTime(): #create new list and replace cron syntax with times. Siia TODO
    #TODO better solution, better regex
    orderedList = []
    for line in getCronEntries(): #convert cron syntax to time
        muutuja = re.match('^((?:[^ ]* ){4}[^ ]*)',line).group(0)
        muutuja2 = str(getTime(muutuja)) #hack
        line = line.replace(muutuja, muutuja2)
        orderedList.append(line)
    return orderedList

def sortByTime(list):
    return sorted(list)

def sortByTimeReverse(list):
    return sorted(list, reversed)

'''
for line in sortByTime(syntaxToTime()):
    print line
'''
getTime("*/30 * * * *")