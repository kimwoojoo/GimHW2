import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
import threading 
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

class Check(threading.Thread):
	def run(self):
		CheckSenSor()
	def stop(self):
		self._stop.set()
	def stopped(self):
		return self._stop.isSet()

class Check2(threading.Thread):
	def run(self):
		CheckSenSor2()
	def stop(self):
		self._stop.set()
	def stopped(self):
		return self._stop.isSet()

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


#Grenn LED
def CheckSenSor():
	SwitchMode()


#RED and Yellow LED

def CheckSenSor2():
	SwitchMode()
	HuManSenSor()


def RLed():
	th = Check2()
	th.start()
	print 'Red Led On\n'
	GPIO.output(RedPin, GPIO.HIGH)
	time.sleep(3)
	print 'Red Led OFF\n'
	GPIO.output(RedPin, GPIO.LOW)
	time.sleep(1)

def GLed():
	Th = Check()
	Th.start()
	print 'Green Led On\n'
	GPIO.output(GreenPin, GPIO.HIGH)
	time.sleep(3)
	print 'Green Led OFF\n'
	GPIO.output(GreenPin, GPIO.LOW)
	time.sleep(1)

def YLed():
	th = Check2()
	th.start()
	print 'Yellow Led On\n'
	GPIO.output(YellowPin, GPIO.HIGH)
	time.sleep(3)
	print 'Yellow Led OFF\n'
	GPIO.output(YellowPin, GPIO.LOW)
	time.sleep(1)

def HuManSenSor():
	HValue = GPIO.input(HumanPin)
	if(HValue == GPIO.HIGH):
		print "Motion DeTecTing\n"
		printUltra()
		GPIO.output(BuzzerPin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(BuzzerPin, GPIO.LOW)
		time.sleep(1)

def SwitchMode():
	SValue = GPIO.input(SwitchPin)
	if(SValue == GPIO.HIGH):
		print 'Switch On\nTemperature and Humidity print\n'
		printTempHumi()
		
	return SValue

def printTempHumi():
	time.sleep(0.5)
	h,t = dht.read_retry(dht.DHT11, TempPin)
	print 'Temperature = {0:0.1f}*C\n Humidity = {1:0.1f}%\n'.format(t,h)

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

	print "Distance Between Human Sensor and Person : ", Distance , "CM\n" 

try:
	while True:
		Setup()
		RLed()
		time.sleep(1)
		YLed()
		time.sleep(1)
		GLed()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print 'GoodBye'


