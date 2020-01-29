# Pomodoro Timer

from time import sleep
import os

longDuration = 25 #1500
shortDuration = 5 #300 #input("Choose a break time (3-5 minutes).")
iterations = 0
longBreak = 30 #1800
firstTime = True


def longDurationFunc():
    sleep(longDuration)
    os.system('say "Take a break"')


def breakFunc(longBreak):
    if longBreak:
        sleep(longBreak)
    else:
        sleep(longDuration)
    os.system('say "Back to work"')


while True:
    if firstTime:
        firstTime = False
        longDurationFunc()
        iterations = iterations + 1
    while iterations < 4:
        breakFunc(False)
        longDurationFunc()
        iterations = iterations + 1
    iterations = 0
    if input("Continue (after a break)? y/n     ") == "y":
        breakFunc(True)
        firstTime = True
    else:
        break


