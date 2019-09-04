# PythonStudentGeolocation

Tis project sample contains the solutions for the exercise 2:

Problem 2:
Given each student has a geolocation lat/lon point, how would you determine which students
are physically in any classroom?
Write a function that returns the students if they are in a classroom.

There are 2 python files which can be run to see the core functionality
 - Exercises.py
 - Bonus.py
 
### Execution ###
- execute the command: 

  - ``` python Exercises.py ```

  - ``` python Bonus.py ```

### Testing ###
Please see the console output in order to review results after execution 

### Library Reference ###

-----------------
This implementation uses third party code:
- Piece of code [BoundingBox](https://stackoverflow.com/questions/1648917/given-a-latitude-and-longitude-and-distance-i-want-to-find-a-bounding-box)

``` 
 It was modified to work with a variation in variables and values from:
 def get_bounding_box(latitude_in_degrees, longitude_in_degrees, half_side_in_miles):
 to:
 def getBoundingBox(latitude_in_degrees, longitude_in_degrees, half_side_in_meters):
```
