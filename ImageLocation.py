import PIL.Image
import PIL.ExifTags
import os
import os.path
class Image:
   'Common base class for all employees'
   

   def __init__(self, location):
      self.location = location

   def getLocation(self):
       return os.listdir(self.location)
   def extractData(self):
       images = self.getLocation()
       gpsLocation = []
       directory = os.path.dirname(os.path.abspath(__file__))
       print(directory)
       
       for image in images: 
           img = PIL.Image.open(os.path.join(directory, "images" ,image))
           exif = {
                     PIL.ExifTags.TAGS[k]: v
                     for k, v in img._getexif().items()
                        if k in PIL.ExifTags.TAGS
                    }
           gpsLocation.append(exif['GPSInfo'])
       return gpsLocation
           
           

   def __str__(self):
       return str(self.location)
      

image = Image("images")
print(image)
print(image.getLocation())
print(image.extractData())



