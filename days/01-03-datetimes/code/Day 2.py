from datetime import datetime, timedelta
from datetime import date


#bite 128


myStrDate = '11/03/2002'
print("testing")
print(datetime.strptime(myStrDate, '%d/%m/%Y'))
print(datetime.strptime(myStrDate, '%d%/%m/%Y').strftime('%m/%d/%Y'))
mydate = datetime.strptime(myStrDate, '%d $b, %Y').year
print(mydate)



#bite 67

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


mydate = start_100days + timedelta(days=100)
print(mydate)
print(date.__format__(mydate, "yyyy-mm-dd"))
print(mydate.strftime("%Y-%m-%d"))

print((pycon_date - pybites_founded).days)

# DAY 2 - Bite 7 Parsing dates from logs

from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()

print(loglines)



# for you to code:

def convert_to_datetime(line):
    return datetime.strptime(line.split()[1], "%Y-%m-%dT%H:%M:%S")
    pass

print(convert_to_datetime(loglines[len(loglines) - 1]))
print(convert_to_datetime(loglines[0]))
print(convert_to_datetime(loglines[len(loglines)-1]) - convert_to_datetime(loglines[0]))
firststring = ""
laststring = ""
for line in loglines:
    if line.split()[3] == "Shutdown" and line.split()[4] == "initiated.":
        if firststring == "":
            firststring = line
        else:
            laststring = line
print(convert_to_datetime(laststring) - convert_to_datetime(firststring))
print("frist string is " + firststring)
print("second string is " + laststring)

def time_between_shutdowns(loglines):
    print(convert_to_datetime(loglines[len(loglines) - 1]) )
    print(convert_to_datetime(loglines[0]))

    return loglines[len(loglines)-1] - loglines[0]
    pass


def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    print(loglines)
    diff = time_between_shutdowns(loglines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'