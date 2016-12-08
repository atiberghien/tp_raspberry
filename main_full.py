#!/usr/bin/python
# coding: utf-8

from utils import *

import RPi.GPIO as GPIO
import time
import tweepy

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def exo1():
    #Allumer la LED
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8,True)

def exo2():
    #Faire clignoter la LED
    GPIO.setup(8, GPIO.OUT)
    while True:
        GPIO.output(8,True)
        time.sleep(1)
        GPIO.output(8,False)
        time.sleep(1)

def exo3():
    #Le chenillard, faire clignoter successivement 3 LED
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    while True:
        GPIO.output(8,True)
        time.sleep(1)
        GPIO.output(8,False)
        time.sleep(1)
        GPIO.output(10,True)
        time.sleep(1)
        GPIO.output(10,False)
        time.sleep(1)
        GPIO.output(12,True)
        time.sleep(1)
        GPIO.output(12,False)
        time.sleep(1)

def exo4():
    #Allumer la LED grace à un bouton poussoir
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        etat = GPIO.input(16)
        if etat == False:
            GPIO.output(8, True)
        else:
            GPIO.output(8, False)
        time.sleep(0.2)

def exo5():
    #Allumer la LED en fonction de la luminosité ambiante en utilisant la fonction read_light
    while True:
        light = read_light(7)
        if light > 400:
            GPIO.output(8, GPIO.HIGH)
        else:
            GPIO.output(8, GPIO.LOW)

def exo6():
    #Relever la température ambiante
    while True:
        print read_temp()

def exo7(my_flower_name):

    auth = tweepy.OAuthHandler("LGR9nWvXLNZbi7fHbyXojUCky", "tkkwd6CRSFFQY0cKT3S5qm4HoVCJReIa1EUXvamrwCk1OXCjxv")
    auth.set_access_token("777822224296411136-PqlOUsqej0K1vRsI6zt2WbkVc5Qo3JS", "xx5KUdBDVP2cHpT33W4ys9HQRZcvg1RYeZUn8HXCdGlut")
    api = tweepy.API(auth)

    last_mention_id = None

    while True:

        most_recent_mention = api.mentions_timeline(count=1)[0]

        if last_mention_id == None:
            last_mention_id = most_recent_mention.id
        elif last_mention_id != most_recent_mention.id:
            supervisor, flower_name, action, hour = most_recent_mention.text.split(" ")
            if my_flower_name in flower_name:
                if action == "#temperature":
                    api.update_status(status="@%s %s %sC %s" %(most_recent_mention.user.screen_name,
                                                               flower_name, read_temp(),
                                                               time.strftime('%d/%m/%Y %Hh%M')))

            last_mention_id = most_recent_mention.id

        time.sleep(10)


# exo1()
# exo2()
# exo3()
# exo4()
# exo5()
# exo6()
exo7("jean")
