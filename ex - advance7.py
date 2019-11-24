class Student:
    def __init__(self,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
class School:
    def __init__(self):
        self.students = []

    def addStudent(self,student):
        self.students.append(student)

    def get_age_avg(self):
        age_avg = float()
        for i in range (0,len(self.students)):
            age_avg = age_avg + float(self.students[i].age)
        return age_avg/len(self.students)

    def get_height_avg(self):
        hight_avg = float()
        for i in range (0,len(self.students)):
            hight_avg = hight_avg + float(self.students[i].height)
        return hight_avg/len(self.students)


    def get_weight_avg(self):
        weight_avg = float()
        for i in range (0,len(self.students)):
            weight_avg = weight_avg + float(self.students[i].weight)
        return weight_avg/len(self.students)
    
def compare_avg_height(schoolA,schoolB):
    if schoolA.get_height_avg() > schoolB.get_height_avg():
        return "A"
    elif schoolA.get_height_avg() < schoolB.get_height_avg():
        return "B"
    else:
        if schoolA.get_weight_avg() > schoolB.get_weight_avg():
            return "B"
        elif schoolA.get_weight_avg() < schoolB.get_weight_avg():
            return "A"
        elif (schoolA.get_height_avg() == schoolB.get_height_avg()) and (schoolA.get_weight_avg() == schoolB.get_weight_avg()):
            return "Same"


list_age = []
list_height = []
list_weight = []


schoolA=School()


student_len_school_a = int(input())
list_age_A = [int(x) for x in input().split()]
list_height_A = [int(x) for x in input().split()]
list_weight_A = [int(x) for x in input().split()]

for i in range(0,student_len_school_a):
    student=Student(list_age_A[i],list_height_A[i],list_weight_A[i])
    schoolA.addStudent(student)


schoolB=School()
student_len_school_b = int(input())
list_age_B = [int(x) for x in input().split()]
list_height_B = [int(x) for x in input().split()]
list_weight_B = [int(x) for x in input().split()]


for i in range(0,student_len_school_b):
    student=Student(list_age_B[i],list_height_B[i],list_weight_B[i])
    schoolB.addStudent(student)

print(schoolA.get_age_avg())
print(schoolA.get_height_avg())
print(schoolA.get_weight_avg())
print(schoolB.get_age_avg())
print(schoolB.get_height_avg())
print(schoolB.get_weight_avg())
print(compare_avg_height(schoolA,schoolB))