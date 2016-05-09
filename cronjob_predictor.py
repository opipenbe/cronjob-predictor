#!/usr/bin/python

__author__ = 'Olari Pipenberg'

import subprocess
import re
import argparse
from croniter import croniter
from datetime import datetime

# Lets add some arguments...
parser = argparse.ArgumentParser()
parser.add_argument("-cmd", help="show cronjob time and corresponding command",
                    action="store_true")
parser.add_argument("-user", help="specify cron table user")
args = parser.parse_args()

# Functions

def get_cron_table(): # read crontab output into variable
    try:
        if args.user:
            cron_table = subprocess.check_output('crontab -l', shell=True)
        else:
            cron_table = subprocess.check_output('crontab -l', shell=True)
    except: # no cron entries
        raise
        exit(1)
    return cron_table

def find_cron_jobs(cron_table): # append cronjob lines into list
    lines = []
    for line in cron_table.splitlines():
        line = line.lstrip() # remove leading whitespaces
        if validate_cron_syntax(line) == True:
            lines.append(line)
    return lines

def validate_cron_syntax(cron_line): # validates correct crontab lines
    if not cron_line.strip(): # check for empty lines
        return False
    if cron_line.startswith("#"): # check if it is not comment
        return False
    if cron_line.startswith("@"): # check if it is special string
        print("Crontab entry contains special string(s). Sorry is not supported yet :(") #TODO?
        exit(1)
    return True

def get_time(cron_format, base = datetime.now()):
    try:
        iter = croniter(cron_format, base)
    except ValueError:
        print "Program experienced error with crontab syntax. Sorry :("
        exit(1)
    clock = iter.get_next(datetime) #time global var and next time?
    return clock

def syntax_to_time(cronjob_line_list, show_time_only=True, time_base = datetime.now()): #create new list and replace cron syntax with times.
    converted_list = []
    for line in cronjob_line_list: #convert cron syntax to time
        cron_syntax = re.match('^([\S]+[\s]{1,}){4}[\S]+',line).group(0) #find cron syntax
        converted_time = str(get_time(cron_syntax, base=time_base))
        if show_time_only == False:
            line = converted_time
        else:
            line = line.replace(cron_syntax, converted_time)
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

    show_cmd = False
    if args.cmd:
        show_cmd = True

    cron_table = get_cron_table()
    cron_jobs = find_cron_jobs(cron_table)

    converted_jobs = syntax_to_time(cron_jobs, show_time_only=show_cmd)
    cron_jobs = sort_by_time(converted_jobs)
    #print first_cron_job(cron_jobs)
    for job in cron_jobs:
        print job

# TODO manual
#exit cmd
#users
# date -d"2016-05-07 05:00:00" +%d