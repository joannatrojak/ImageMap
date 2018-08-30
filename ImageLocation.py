from GPSPhoto import gpsphoto
import os
import os.path
class Image:
   def __init__(self, location):
      self.location = location

   def getLocation(self):
       return os.listdir(self.location)
   def extractData(self):
       images = self.getLocation()
       gpsLocation = []
       directory = os.path.dirname(os.path.abspath(__file__))
      
       for image in images: 
        print(gpsphoto.getGPSData(image))
   
           
           

   def __str__(self):
       return str(self.location)
      

image = Image("images")
print(image)
print(image.getLocation())
print(image.extractData())
print(image.convertToDegrees())



