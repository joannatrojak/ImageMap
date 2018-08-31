import PIL.Image
import PIL.ExifTags
import os
import os.path
class Image:
   def __init__(self, location):
      self.location = location 
   def __call__(self, location):
       print location
   def getLocation(self, image):
       directory =  os.path.dirname(os.path.abspath(__file__)) + '/images/'
       img = PIL.Image.open(directory + image)
       print(img)
       exif = {
                     PIL.ExifTags.TAGS[k]: v
                     for k, v in img._getexif().items()
                        if k in PIL.ExifTags.TAGS
                    }
       gpsinfo = {}
       for key in exif['GPSInfo'].keys():
           decode = PIL.ExifTags.GPSTAGS.get(key,key)
           gpsinfo[decode] = exif['GPSInfo'][key]

       latitudeRef = gpsinfo['GPSLatitudeRef']
       latitude = self.converToDegrees(gpsinfo['GPSLatitude'])
       longitudeRef = gpsinfo['GPSLongitudeRef']
       longitude = self.converToDegrees(gpsinfo['GPSLongitude'])

       return latitudeRef + ' ' + str(latitude) + ' ' + longitudeRef + ' ' + str(longitude)
       

       
   def converToDegrees(self, value):
       d0 = value[0][0]
       d1 = value[0][1]
       d = float(d0) / float(d1)

       m0 = value[1][0]
       m1 = value[1][1]
       m = float(m0) / float(m1)

       s0 = value[2][0]
       s1 = value[2][1]
       s = float(s0) / float(s1)

       return d + (m / 60.0) + (s / 3600.0)
       
   
          
           
           
   def __str__(self):
       return str(self.location)
      






