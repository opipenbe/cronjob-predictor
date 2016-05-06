__author__ = 'Olari Pipenberg'

import subprocess
import re
from croniter import croniter
from datetime import datetime

#Todo time scheduling

#Todo arguments, users, entry print

#date -d"2016-05-07 05:00:00" +%d

def getCronTable(): #read crontab output into variable
    try:
        cronTable = subprocess.check_output('crontab -l', shell=True)
    except: #no cron entries
        quit()
    return cronTable

def findCronJobs(cronVar): #append cronjob lines into list
    cronTable = cronVar
    lines = []
    for line in cronTable.splitlines():
        line = line.lstrip() #remove leading whitespaces
        if validateCronEntry(line) == True:
            lines.append(line)
    return lines

def validateCronEntry(cronLine): #validates correct crontab lines
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
    base = datetime.now() #get current system time
    #print "Current time:",base
    iter = croniter(cronFormat, base)
    #TODO error handling, time global var?
    aeg = iter.get_next(datetime)
    #Todo next
    return aeg

def syntaxToTime(cronJobLines): #create new list and replace cron syntax with times. Siia TODO
    #TODO better solution, better regex
    orderedList = []
    for line in cronJobLines: #convert cron syntax to time
        muutuja = re.match('^((?:[^ ]* ){4}[^ ]*)',line).group(0)
        muutuja2 = str(getTime(muutuja)) #hack
        line = line.replace(muutuja, muutuja2)
        orderedList.append(line)
    return orderedList

def sortByTime(list):
    return sorted(list)

def firstCronJob(list):
    return (list[:1] or "") #"" means in case crontab is empty


if __name__ == "__main__":
    cronTable = getCronTable()
    cronJobs = findCronJobs(cronTable)
    convertedJobs = syntaxToTime(cronJobs)
    cronJobs = sortByTime(convertedJobs)
    print firstCronJob(cronJobs)

