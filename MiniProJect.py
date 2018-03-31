import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

#define Pin Number
HumanPin = 17
TempPin = 2
BuzzerPin =4
RedPin = 16
YellowPin = 20
GreenPin = 21
SwitchPin = 27
TrigPin = 23
EchoPin = 24

#define Pin`s Setup 
def Setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.setup(HumanPin, GPIO.IN)
	GPIO.setup(RedPin, GPIO.OUT)
	GPIO.setup(YellowPin, GPIO.OUT)
	GPIO.setup(GreenPin, GPIO.OUT)
	GPIO.setup(SwitchPin, GPIO.IN)
	GPIO.setup(TrigPin, GPIO.OUT)
	GPIO.setup(EchoPin, GPIO.IN)
	
#define Switch On and OFF Check and HumanSenSor Check
def CheckSenSor():
	SwitchMode()
	HuManSenSor()

#define Red Led 
def RLed():
	print 'Red Led On'
	CheckSenSor()
	GPIO.output(RedPin, GPIO.HIGH)
	time.sleep(3)
	print 'Red Led OFF'
	GPIO.output(RedPin, GPIO.LOW)
	time.sleep(1)

#define Green Led
def GLed():
	print 'Green Led On'
	CheckSenSor()
	GPIO.output(GreenPin, GPIO.HIGH)
	time.sleep(3)
	print 'Green Led OFF'
	GPIO.output(GreenPin, GPIO.LOW)
	time.sleep(1)

#define Yellow Led
def YLed():
	print 'Yellow Led On'
	CheckSenSor()
	GPIO.output(YellowPin, GPIO.HIGH)
	time.sleep(3)
	print 'Yellow Led OFF'
	GPIO.output(YellowPin, GPIO.LOW)
	time.sleep(1)

#define HuManSenSor Detecting
def HuManSenSor():
	HValue = GPIO.input(HumanPin)
	if(HValue == GPIO.HIGH):
		print "Motion DeTecTing"
		printUltra()
		GPIO.output(BuzzerPin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(BuzzerPin, GPIO.LOW)
		time.sleep(1)

#define Switch Push and Pull Detecting
def SwitchMode():
	SValue = GPIO.input(SwitchPin)
	if(SValue == GPIO.HIGH):
		print 'Switch On\nTemperature and Humidity print'
		printTempHumi()
		
	return SValue

#define Print Temperature and Humidity 
def printTempHumi():
	time.sleep(0.5)
	h,t = dht.read_retry(dht.DHT11, TempPin)
	print 'Temperature = {0:0.1f}*C\n Humidity = {1:0.1f}%'.format(t,h)

#define Print Distance
def printUltra():
	GPIO.output(TrigPin, GPIO.LOW)
	time.sleep(0.3)
	GPIO.output(TrigPin, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(TrigPin, GPIO.LOW)
	while GPIO.input(EchoPin)==0:
		pulse_start = time.time()
	while GPIO.input(EchoPin)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	Distance = pulse_duration * 17150
	Distance = round(Distance,2)

	print "Distance Between Human Sensor and Person : ", Distance , "CM" 
	
#define Main Method
try:
	while True:
#PinSetup
		Setup()
#Each Led Method Call
		RLed()
		time.sleep(1)
		YLed()
		time.sleep(1)
		GLed()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print 'GoodBye'

'''
while True:
	h, t = dht.read_retry(dht.DHT11, TempPin)
	print 'temp = {0:0.1f}*C Humidity = {1:0.1f}%'.format(t,h)
	time.sleep(1)
'''

