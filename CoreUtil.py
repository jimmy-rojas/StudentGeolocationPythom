
import math

class BoundingBox(object):
 def __init__(self, *args, **kwargs):
  self.lat_min = None
  self.lon_min = None
  self.lat_max = None
  self.lon_max = None

 def hasWithin(self, student):
  return self.lat_min <= student["latitude"] <= self.lat_max and self.lon_min <= student["longitude"] <= self.lon_max


def get_bounding_box(latitude_in_degrees, longitude_in_degrees, half_side_in_meters):
 assert half_side_in_meters > 0
 assert latitude_in_degrees >= -90.0 and latitude_in_degrees <= 90.0
 assert longitude_in_degrees >= -180.0 and longitude_in_degrees <= 180.0

 half_side_in_km = (half_side_in_meters/1000.0)
 lat = math.radians(latitude_in_degrees)
 lon = math.radians(longitude_in_degrees)

 radius = 6371
 # Radius of the parallel at given latitude
 parallel_radius = radius * math.cos(lat)

 lat_min = lat - half_side_in_km / radius
 lat_max = lat + half_side_in_km / radius
 lon_min = lon - half_side_in_km / parallel_radius
 lon_max = lon + half_side_in_km / parallel_radius
 rad2deg = math.degrees

 box = BoundingBox()
 box.lat_min = rad2deg(lat_min)
 box.lon_min = rad2deg(lon_min)
 box.lat_max = rad2deg(lat_max)
 box.lon_max = rad2deg(lon_max)

 return (box)


def studentsInClasses(StudentList, ClassroomList):
 #return [student for student in StudentList for classroom in ClassroomList if(studentInClass(student, classroom))]
 result = []
 for student in StudentList:
  for classroom in ClassroomList:
    box = get_bounding_box(classroom["latitude"], classroom["longitude"], 10)
    if(box.hasWithin(student)):
     result.append(student)
 return result


StudentList = []
StudentFoundList = []
ClassroomList = []

#-- sample 1
engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }

john_student = { 'name': 'John Wilson', 'latitude': 34.069149, 'longitude': -118.442639 } #engineering
jane_student = { 'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862 } #geology
pam_student = { 'name': 'Pam Bam', 'latitude': 34.071513, 'longitude': -118.441181 } #humanities

student_list = [john_student,jane_student,pam_student]
classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]

StudentFoundList = studentsInClasses(student_list, classroom_list)

print(len(StudentFoundList))
print(StudentFoundList)

ExpectedList = [
 {'latitude': 34.069149, 'name': 'John Wilson', 'longitude': -118.442639},
 {'latitude': 34.069601, 'name': 'Jane Graham', 'longitude': -118.441862},
 {'latitude': 34.071513, 'name': 'Pam Bam', 'longitude': -118.441181}
]

assert(ExpectedList == StudentFoundList)

#-- sample 2
engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }

john_student = { 'name': 'John Wilson', 'latitude': 34.069849, 'longitude': -118.443539 } #engineering
jane_student = { 'name': 'Jane Graham', 'latitude': 34.069901, 'longitude': -118.441562 } #geology
pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } #humanities

classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]
student_list2 = [john_student,jane_student,pam_student]

StudentFoundList = studentsInClasses(student_list2, classroom_list)

print(len(StudentFoundList))
print(StudentFoundList)

ExpectedList = [
 {'latitude': 34.071523, 'name': 'Pam Bam', 'longitude': -118.441171}
]

assert(ExpectedList == StudentFoundList)
