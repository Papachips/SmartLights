#! /usr/bin/python3

from pyvesync import VeSync
import time
from suntime import Sun
from datetime import datetime, timezone
from pywizlight.bulb import wizlight, PilotBuilder
from enum import Enum
import pyowm

def loginAPI():
    #Username/password for Vesync.
    user = VESYNC_USER
    password = VESYNC_PW
    api = VeSync(user,password)
    api.login()
    api.update()
    return api

def loginInfo():
    print('Job run at: ' + str(datetime.now()))

def calculateSunset():
    #Information for Suntime to calculate sunset.
    latitude = LATITUDE
    longitude = LONGITUDE
    sun = Sun(latitude, longitude)
    sunset = sun.get_local_sunset_time()
    return sunset

def getWeather():
    owm = pyowm.OWM(WEATHER_API_KEY)
    manager = owm.weather_manager()
    observation = manager.weather_at_place(LOCATION)
    weather = observation.weather
    return weather

#Wiz functions
async def turnLightOn(light):
    await light.turn_on(PilotBuilder())

async def turnLightOff(light):
    await light.turn_off()

#brightnessValue can be 0 - 255.
async def setLightBrightness(light, brightnessValue):
    await light.turn_on(PilotBuilder(brightness = brightnessValue))

#red value can be 0 - 255.
#green value can be 0-255.
#blue value can be 0-255.
async def setRGBColors(light, red,green,blue):
    await light.turn_on(PilotBuilder(rgb = (red,green,blue)))

async def setLightScene(light, sceneNumber):
    await light.turn_on(PilotBuilder(scene=sceneNumber))

class Scenes(Enum):
    OCEAN = 1
    ROMANCE = 2
    SUNSET = 3
    PARTY = 4
    FIREPLACE = 5
    COZY = 6
    FOREST = 7
    PASTEL = 8
    WAKEUP = 9
    BEDTIME = 10
    WARM_WHITE = 11
    DAY_LIGHT = 12
    COOL_WHITE = 13
    NIGHT_LIGHT = 14
    FOCUS = 15
    RELAX = 16
    TRUE_COLORS = 17
    TV_TIME = 18
    PLANT_GROWTH = 19
    SPRING = 20
    SUMMER = 21
    FALL = 22
    DEEP_DIVE = 23
    JUNGLE = 24
    MOJITO = 25
    CLUB = 26
    CHRISTMAS = 27
    HALLOWEEN = 28
    CANDLE = 29
    GOLDEN_WHITE = 30
    PULSE = 31
    STEAMPUNK = 32