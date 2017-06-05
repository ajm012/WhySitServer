#!/usr/bin/python

import sys, os
import cgi, cgitb
import csv

print 'Content-type: text/html\n\n'

form = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'] == 'POST':
    print 'Post request received.'

    data = (str(form.getvalue("time")),
	    str(form.getvalue("Q1")),
	    str(form.getvalue("Q2")),
            str(form.getvalue("Q3")),
            str(form.getvalue("Q4")),
            str(form.getvalue("Q5")),
            str(form.getvalue("Q6a")),
            str(form.getvalue("Q6b")),
            str(form.getvalue("Q6c")),
            str(form.getvalue("Q6d")),
            str(form.getvalue("Q7a")),
            str(form.getvalue("Q7b")),
            str(form.getvalue("latitude")),
            str(form.getvalue("longitude")))
    survey_number = str(form.getvalue("survey"))
    id = str(form.getvalue("id"))
    PATH_OUTPUT = 'Results' #'~/ajm012/www/Results/'
    if not os.path.exists(PATH_OUTPUT):
        os.makedirs(PATH_OUTPUT)
    BACKUP = 'Backup' #'~/ajm012/www/Backup/'
    if not os.path.exists(BACKUP):
	os.makedirs(BACKUP)
    FILE_NAME = "Results/"+id+"_surveys.csv"
    writer = csv.writer(open(FILE_NAME,"a"))
    writer.writerow(data)
    BACKUP_NAME = "Backup/Survey"+survey_number+".csv"
    writer = csv.writer(open(BACKUP_NAME, "a"))
    writer.writerow(data)
    print 'Done.'
