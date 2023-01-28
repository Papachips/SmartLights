#! /usr/bin/python3

import MasterFunctions as master
from datetime import datetime
from pywizlight.bulb import wizlight, PilotBuilder
import traceback
import asyncio

#weather api likes to fail on the first attempt at times so we try twice
tries = 0

while tries < 2:
    try:
        #Login to VesyncApi.
        api = master.loginAPI()
        if api:
            master.loginInfo()
            
            #Plugs for vesync
            christmasTree = api.outlets[0]
            officeLamp = api.outlets[1]
            dehumidifer = api.outlets[2]
            basementLights = api.outlets[3]
            foyerLamp = api.outlets[4]
            diningRoomLamp = api.outlets[5]

            #Wiz bulbs
            livingRoomLamp = wizlight(LOCAL_ADDRESS)
            bedroomLamp = wizlight(LOCAL_ADDRESS)
            scenes = master.Scenes

            sunset = master.calculateSunset().timestamp()
            currentTime = datetime.now().timestamp()
            weather = master.getWeather()

            if('rain' in weather.status.lower() or
            'drizzle' in weather.status.lower()  or
            'thunderstorm' in weather.status.lower()  or
            'snow' in weather.status.lower()  or
            'broken' in weather.detailed_status.lower() or
            'overcast' in weather.detailed_status.lower()):
                    officeLamp.turn_on()
                    christmasTree.turn_on()
                    foyerLamp.turn_on()
                    asyncio.run(master.setLightScene(livingRoomLamp, 6))
                    print('Lights turned on for weather successfully')

            if(currentTime >= sunset):
                officeLamp.turn_on()
                diningRoomLamp.turn_on()
                christmasTree.turn_on()
                foyerLamp.turn_on()
                asyncio.run(master.setLightScene(livingRoomLamp, 6))
                asyncio.run(master.setLightBrightness(livingRoomLamp, 255))
                asyncio.run(master.setLightScene(bedroomLamp, 6))
                asyncio.run(master.setLightBrightness(bedroomLamp, 125))
                print('Lights turned on for sunset succesfully')
            tries = 2
    except:
        print(traceback.format_exc())
        tries = tries + 1

