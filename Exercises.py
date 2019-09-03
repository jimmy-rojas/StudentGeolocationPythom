import Data
from BoundingBox import BoundingBox

def studentsInClasses(StudentList, ClassroomList):
 result = []
 for student in StudentList:
  for classroom in ClassroomList:
    box = BoundingBox.getBoundingBox(classroom["latitude"], classroom["longitude"], 10)
    if(box.hasWithin(student)):
     result.append(student)
 return result
 #TODO: need review a better approach
 #return [student for student in StudentList for classroom in ClassroomList if(studentInClass(student, classroom))]

StudentFoundList = []

#-- sample 1
print("------ Sample 1")
StudentFoundList = studentsInClasses(Data.student_list, Data.classroom_list)
print(len(StudentFoundList))
print(StudentFoundList)

ExpectedList = [
 {'latitude': 34.069149, 'name': 'John Wilson', 'longitude': -118.442639},
 {'latitude': 34.069601, 'name': 'Jane Graham', 'longitude': -118.441862},
 {'latitude': 34.071513, 'name': 'Pam Bam', 'longitude': -118.441181}
]

assert(len(ExpectedList) == len(StudentFoundList))
assert(ExpectedList == StudentFoundList)

#-- sample 2

print("------ Sample 2")
StudentFoundList = studentsInClasses(Data.student_list2, Data.classroom_list2)
print(len(StudentFoundList))
print(StudentFoundList)

ExpectedList = [
 {'latitude': 34.071523, 'name': 'Pam Bam', 'longitude': -118.441171}
]
assert(len(ExpectedList) == len(StudentFoundList))
assert(ExpectedList == StudentFoundList)
