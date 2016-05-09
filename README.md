# README #

This script reads current system crontab and outputs nearest cronjob.

#Requirements

Python 2.7

croniter

#Installation

*sudo pip install croniter*

#Usage

cronjob_predictor.py [-h] [-cmd] [-user USER]

#Examples:

Output root user nearest cronjob

             *sudo python cronjob_predictor.py -user=root*

UNIX date command in conjuction with this script:

             *date -d"$(python cronjob_predictor.py)" +%H:%m*