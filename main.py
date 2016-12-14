#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
import tweepy
import utils
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def exo1():
    #Allumer la LED
    pass

def exo2():
    #Faire clignoter la LED
    pass

def exo3():
    #Le chenillard, faire clignoter successivement 3 LED
    pass

def exo4():
    #Allumer la LED grace à un bouton poussoir
    pass

def exo5():
    #Allumer la LED en fonction de la luminosité ambiante en utilisant la fonction read_light
    pass

def exo6():
    #Relever la température ambiante
    pass

def exo7(my_flower_name):
    #Surveiller les mentions twitters du compte @FlowersGlouGlou
    #et en fonction de nom de plante demandée envoyé un twitter avec la température ambiance
    pass


# exo1()
# exo2()
# exo3()
# exo4()
# exo5()
# exo6()
# exo7("jean")
