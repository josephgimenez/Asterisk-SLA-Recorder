#!/usr/bin/python

import commands
import re
import shutil
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.message import Message
from email import encoders
from email.utils import COMMASPACE
import mimetypes

#curDate = datetime.datetime.now() - datetime.timedelta(x)

#Get current date
curDate = datetime.datetime.now()
curDate = curDate.strftime("%Y-%m-%d - %H:%M")

#Assign path to SLA record file
SLAFile = "/root/sla-record"

try:
  report = open(SLAFile, "a")

except:
  print "Unable to open SLA file."

#Find service level information
queue = commands.getoutput("/usr/sbin/asterisk -r -x 'queue show 5000'").split('\n')
servicelevel = re.search("SL:(\d+\.\d+)% within (\d+)s", queue[0])
holdtime = re.search("(\d+)s holdtime", queue[0])

report.write("Date/Time: " + curDate + "\n")
report.write("Service level: " + servicelevel.group(1) + "% of calls answered within " + servicelevel.group(2) + "\n")
report.write("Hold time average: " + holdtime.group(1) + " seconds \n\n")

report.close()
