
import math

class BoundingBox(object):
 def __init__(self, *args, **kwargs):
  self.lat_min = None
  self.lon_min = None
  self.lat_max = None
  self.lon_max = None

 def hasWithin(self, student):
  return self.lat_min <= student["latitude"] <= self.lat_max and self.lon_min <= student["longitude"] <= self.lon_max

 @staticmethod
 def getBoundingBox(latitude_in_degrees, longitude_in_degrees, half_side_in_meters):
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
