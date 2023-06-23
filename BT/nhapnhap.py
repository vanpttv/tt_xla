import serial
# import RPi.GPIO as GPIO
import os, time, sys
# from geopy.geocoders import Nominatim

# GPIO.setmode(GPIO.BOARD)

# Enable Serial Communication
port1 = "/dev/ttyUSB0"
port2 = "/dev/ttyS0"    # Raspberry Pi 3 / Pi Zero / Pi Zero W

def parseGPS(data):
	while data[0:6] != "$GPGGA":
		data = ser2.readline()
	s = data.split(",")
	if s[7] == '0':
		print("Satellite Data Not Available")
		return "Satellite Data Not Available"
	time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
	lat = decode(s[2])
	dirLat = s[3]
	lon = decode(s[4])
	dirLon = s[5]
	alt = s[9] + " m"
	sat = s[7]
	coord = "lat="+lat+"&log="+lon
	print(coord)
	geolocator = Nominatim()
#	location = geolocator.reverse("52.509669, 13.376294")
	ll = lat+", "+lon
	location = geolocator.reverse(ll)
	print(location.address)
	return location.address

def decode(coord):
	# DDDMM.MMMMM -> DD deg MM.MMMMM min
	v = coord.split(".")
	head = v[0]
	tail =  v[1]
	deg = head[0:-2]
	min = head[-2:]
	deg = float(deg)
	mintail = min+"."+ tail
	mintail = float(mintail)
	result = deg + mintail/60
	result = round(result,6)
	return str(result)

ser1 = serial.Serial(port1, baudrate = 9600, timeout = 1)
ser2 = serial.Serial(port2, baudrate = 9600, timeout = 0.5)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

ser1.write('AT'+'\r\n')
ser1.write("\x0D\x0A")
rcv = ser1.read(10)
print(rcv)
time.sleep(3)

ser1.write('ATE0'+'\r\n')                 # Disable the Echo
rcv = ser1.read(10)
print(rcv)
time.sleep(3)

ser1.write('AT+CMGF=1'+'\r\n')            # Select Message format as Text mode
rcv = ser1.read(10)
print(rcv)
time.sleep(3)

ser1.write('AT+CMGDA="DEL ALL"'+'\r\n')
time.sleep(3)
msg = ser1.read(ser1.inWaiting())
print ("Listening for incoming SMS...")
while True:
	msg = ser1.read(ser1.inWaiting())
	if msg != "":
		ser1.write('AT+CMGR=1'+'\r\n')
		time.sleep(3)
		msg = ser1.read(ser1.inWaiting())
		print ("SMS received. Content: ")
		print (msg)
		if "Return Location" in msg:
			try:
				data = ser2.readline()
				MyLocation = parseGPS(data)
			#	MyLocation = "I am testing for Unicode"
			except IndexError:
				MyLocation = "Satellite Data Not Available"
			except ImportError:
				MyLocation = "Satellite Data Not Available"
			except IOError:
				MyLocation = "Satellite Data Not Available"
			except RuntimeError:
				MyLocation = "Satellite Data Not Available"
			ser1.write('AT+CMGS="98XXXXXXXX"'+'\r\n')
			time.sleep(3)
			print("Sending My Location")
			ser1.write(MyLocation.encode()+'\r\n')
			ser1.write("\x1A")
		msg = ''
		time.sleep(3)
		ser1.write('AT+CMGDA="DEL ALL"'+'\r\n')
		time.sleep(3)
		ser1.read(ser1.inWaiting())
	time.sleep(5)