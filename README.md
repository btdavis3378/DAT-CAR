# DAT CAR

## Data Accumulation Through a Car Altering Remote

### Project Objective
Collection and Visualization of Environmental Data with DAT CAR Rover

### Software/Languages/Tools/Hardware Utilized
1. Raspberry Pi 3 B+ with Raspbian
2. Python3 (main script)
3. HTML (for webpage w/ Flask)
4. JavaScript (routing Python functions)
5. Flask (micro web framework)
6. ownCloud (Cloud service)
7. Apache2 (for ownCloud)
8. PhP
9. Ultrasonic Sensor
10. DHT22 (Temp. & Humidity sensor)
11. Pi Camera
12. Portable battery
13. Smart Car Chassis
14. DC Motors
15. Motor Module
16. Jumper Wires/Cables/10k olm resistor
17. 9v Battery

### Purpose
This was a project done in my Networks course at Florida Gulf Coast University during Fall 2019. After the project was finished, the next semester, Spring 2020, the project assignment was to maintain/improve it.

### Current Functionality
DAT CAR is currently able to set up a webserver with Flask to allow a user to control the rover from a computer's web browser. Addtionally, DAT CAR is equipped with a Pi Camera, to allow the user to see where it is going. With Python, the rover can move forwards, backwards, left, and right. DAT CAR is able to collect environment data such as:  distance of an object in front of it, temperature, and humidity of the surrounding area.

### Plans for the Spring 2020 semester
DAT CAR version 1 is being improved to become DAT CAR v2. It was desired that a user be able to access the collected environmental data, so cloud implementation is being worked on. The cloud tool that is being utilized is ownCloud.
<br/> Some of the sub-objectives include:
1. Improve the current database by integrating an SQL or LINQ database
2. Improve the hull integrity of DAT CAR
3. Increase the stability of the camera mount
4. Increase the battery life of the motor module
5. Save images to ownCloud

### Demonstration Video
This following link is a demonstration video of DAT CAR after the Fall 2019 semester. Cloud services were not integrated at this point in time.
<br/> https://youtu.be/Z2ijKjH7bik

### Documentation
I will be adding more documentation to the code as the journey with this project continues.
<br/> The .doc file is the report and documentation for this project during the Networks course during Fall 2019.
