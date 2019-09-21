from time import sleep
from gpiozero import Robot
bot = Robot(left = (7, 8), right = (9, 10)) #7,8,9,10 are the raspberry pie GPIO pin marking
while True:
	bot.forward()
	sleep(3)    #sleep is used to import time
	bot.stop()
	bot.right()
	sleep(1)
	bot.stop()