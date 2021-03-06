from flask import Flask
from flask import render_template, request
from flask import Response
from camera_pi import Camera
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import owncloud

app = Flask(__name__)

#GPIO pins for RC controls
m11=17
m12=22
m21=23
m22=24

#GPIO pins for Ultrasonic Sensor
TRIG = 21 
ECHO = 20

#Setup for temp/humid sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#Set GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Setup for Ultrasonic Sensor
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Setup for RC motors
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
print ("Done with RC Controls & Sensors")

#Read the html file to render web template
a=1
@app.route("/")
def index():
    findDistance()
    findTempHumi()
    return render_template('webPage.html', dist=distance, temp=tempHumi)

#functions to define the movement of the car    
@app.route('/turn_left')
def left_side():
    data1="LEFT"
    GPIO.output(m11 , 0)
    GPIO.output(m12 , 0)
    GPIO.output(m21 , 1)
    GPIO.output(m22 , 0)
    return 'true'

@app.route('/turn_right')
def right_side():
   data1="RIGHT"
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
   return 'true'

@app.route('/go_forward')
def up_side():
   data1="FORWARD"
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   return 'true'

@app.route('/go_backward')
def down_side():
   data1="BACK"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
   return  'true'

#function to calculate the distance in front of the US sensor   
def findDistance():
   GPIO.output(TRIG, False)
   print ("Waiting For Sensor To Settle")
   time.sleep(2)

   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   while GPIO.input(ECHO)==0:
     pulse_start = time.time()

   while GPIO.input(ECHO)==1:
     pulse_end = time.time()

   pulse_duration = pulse_end - pulse_start

   global distance

   distance = pulse_duration * 17150

   distance = round(distance, 2)

   print ("Distance:",distance,"cm")

   return 'true'

#funciton to find the temperature and humidity of area   
def findTempHumi():
   humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
   global tempHumi
   tempHumi = "Temp={0:0.1f}*C  Humidity={1:0.1f}%\n".format(temperature, humidity)
   return 'true'

#Function to save text file to the cloud
#Called from saveSensorData
def saveToCloud():
   oc = owncloud.Client('http://<IPAddress>/owncloud')
   oc.login('username', 'password')
   oc.put_file('testdir/remotefile.txt', 'saved data1.txt')
   link_info = oc.share_file_with_link('testdir/remotefile.txt')
   print ("Here is your link: " + link_info.get_link())

#save sensor data to text file then sends to cloud
@app.route('/save_data')
def saveSensorData():
   findTempHumi()
   findDistance()
   localtime = time.asctime( time.localtime(time.time()) )
   f = open("/home/pi/Documents/DATCAR/saved data1.txt", "a+")
   f.write(localtime + "\n")
   f.write("Distance was %d" % distance + "cm\n")
   f.write(tempHumi + "\n")
   f.close()
   saveToCloud()
   return 'true'
   
#Generate a camera object from Camera import   
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Stream the video to the html file
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#start the web server with flask
if __name__ == "__main__":
 print ("Start")
 app.run(host='0.0.0.0',port=5010, debug=True, threaded=True)
