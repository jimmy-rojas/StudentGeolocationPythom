import Data
from BoundingBox import BoundingBox

#Bonus
def studentClustersInClasses(StudentList, ClassroomList):
 result = []
 classroomDic = {}
 for student in StudentList:
  for classroom in ClassroomList:
    box = BoundingBox.getBoundingBox(classroom["latitude"], classroom["longitude"], 10)
    if(box.hasWithin(student)):
     if (classroom["name"] not in classroomDic):
      classroomDic[classroom["name"]] = []
     classroomDic[classroom["name"]].append(student)

 for key, value in classroomDic.items():
  if (len(value) > 1):
   result = result + value
 return result

print("------ Bonus with Sample 1")
StudentFoundList = studentClustersInClasses(Data.student_list, Data.classroom_list)
print(len(StudentFoundList))
print(StudentFoundList)

print("------ Bonus with Sample 2")
StudentFoundList = studentClustersInClasses(Data.student_list2, Data.classroom_list2)
print(len(StudentFoundList))
print(StudentFoundList)
