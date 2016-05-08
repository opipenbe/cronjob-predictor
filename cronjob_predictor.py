__author__ = 'Olari Pipenberg'

import subprocess
import re
from croniter import croniter
from datetime import datetime

#Todo time scheduling

#Todo arguments, users, entry print

#date -d"2016-05-07 05:00:00" +%d

def get_cron_table(): #read crontab output into variable
    try:
        cron_table = subprocess.check_output('crontab -l', shell=True)
    except: #no cron entries
        quit()
    return cron_table

def find_cron_jobs(cron_table): #append cronjob lines into list
    lines = []
    for line in cron_table.splitlines():
        line = line.lstrip() #remove leading whitespaces
        if validate_cron_syntax(line) == True:
            lines.append(line)
    return lines

def validate_cron_syntax(cron_line): #validates correct crontab lines
    if not cron_line.strip(): #check for empty lines
        return False
    if cron_line.startswith("#"): #check if it is not comment
        return False
    if cron_line.startswith("@"): #check if it is special string
        print("Crontab entry contains special strings. Sorry they are not supported yet :(") #TODO?
        quit(1)
    return True

def get_time(cron_format):
    base = datetime.now() #get current system time
    #print "Current time:",base
    try:
        iter = croniter(cron_format, base)
    except ValueError:
        print "Program experienced error with crontab syntax. Sorry :("
        quit(1)
    aeg = iter.get_next(datetime) #time global var and next time?
    return aeg

def syntax_to_time(cronjob_line_list): #create new list and replace cron syntax with times. Siia TODO
    #TODO better solution, better regex
    converted_list = []
    for line in cronjob_line_list: #convert cron syntax to time
        muutuja = re.match('^([\S]+[\s]{1,}){4}[^ ]',line).group(0)#^((?:[^ ]* ){4}[^ ]*)
        print muutuja
        muutuja2 = str(get_time(muutuja)) #hack
        line = line.replace(muutuja, muutuja2)
        converted_list.append(line)
    return converted_list

def sort_by_time(list):
    return sorted(list)

def first_cron_job(list):
    try:
        job = list[0]
    except IndexError:
        job = ""
    return job

if __name__ == "__main__":
    cron_table = get_cron_table()
    cron_jobs = find_cron_jobs(cron_table)
    converted_jobs = syntax_to_time(cron_jobs)
    cron_jobs = sort_by_time(converted_jobs)
    print first_cron_job(cron_jobs)

