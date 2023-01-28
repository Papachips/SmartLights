#! /usr/bin/python3

from crontab import CronTab
from suntime import Sun
import MasterFunctions as master
from datetime import datetime

cron = CronTab(user=USER)

#Information for Suntime to calculate sunset.
latitude = LATITUDE
longitude = LONGITUDE
sun = Sun(latitude, longitude)
sunset = sun.get_local_sunset_time()

minute = sunset.minute
hour = sunset.hour

weather = master.getWeather()

#set one minute ahead to account for seconds not being less than or equal for code to execute lights
if minute == 0 or minute == 00:
    minute = 1
else:
    minute = minute + 1
    
#convert to string now that we have adjusted
minute = str(minute)
hour = str(hour)

for job in cron:
    if job.comment == 'Turn on Lights':
        job.setall(minute + ' ' + hour + ' * * *')
        cron.write()
        print('Lights job updated: ' + str(datetime.now()))
    if job.comment == 'Turn on Lights Weather':
        if('rain' in weather.status.lower() or
        'drizzle' in weather.status.lower()  or
        'thunderstorm' in weather.status.lower()  or
        'snow' in weather.status.lower()  or
        'broken' in weather.detailed_status.lower() or
        'overcast' in weather.detailed_status.lower()):
            job.setall('00 12 * * *')
            cron.write()
            print('Weather lights job updated: ' + str(datetime.now()))
        else:
            #set job to a date that doesn't exist
            job.setall('00 00 31 2 00')
            cron.write()
            print('Weather jobs reverted: ' + str(datetime.now()))
