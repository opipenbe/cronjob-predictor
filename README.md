# Cronjob_predictor #

This script reads user crontab and outputs nearest cronjob.

#Requirements

Python 2.7

croniter

#Installation

              sudo pip install croniter

#Usage

cronjob_predictor.py [-h] [-cmd] [-user USER]

#Examples:
Output nearest cronjob:

              python cronjob_predictor.py

Output nearest cronjob with corresponding command:

             python cronjob_predictor.py -cmd

Output root user's nearest cronjob:

             sudo python cronjob_predictor.py -user root


UNIX date command in conjuction with this script:

             date -d"$(python cronjob_predictor.py)" +%H:%M

#Licence:
The MIT License (MIT) Copyright (c) 2016 Olari Pipenberg