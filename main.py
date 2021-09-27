import asyncio
import time
import websockets
import json
import RPi.GPIO as GPIO

# Time that you'll get tased in seconds for a miss
taserTimeMiss = 0.05

# Time that you'll get tased in seconds for a level fail
taserTimeFail = 0.05

# If true, only tases when level failed
failMode = False

# Enter the IP of the computer that runs Beat Saber
hostComputerIP = ""
relayPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

if hostComputerIP == "":
    hostComputerIP = input('What is the ip of your Beat Saber machine?: ')

print("HostIP: " + hostComputerIP)


def shockUser(taserTime):
    GPIO.output(relayPin, 1)
    time.sleep(taserTime)
    GPIO.output(relayPin, 0)


def checkData(eventData):
    if (eventData == "failed") and (failMode is True):
        print(eventData)
        shockUser(taserTimeFail)

    if (eventData == "noteMissed") and (failMode is False):
        print(eventData)
        shockUser(taserTimeMiss)

    if eventData == "hello":
        print("Connected")


async def getData():
    GPIO.output(relayPin, 0)
    url = "ws://" + hostComputerIP + ":6557/socket"
    async with websockets.connect(url, max_size=1_000_000_000) as websocket:
        while not websockets.ConnectionClosed:
            data = await websocket.recv()
            data = json.loads(data)
            checkData(data['event'])


asyncio.get_event_loop().run_until_complete(getData())
