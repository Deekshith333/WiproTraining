from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.studentgrade import StudentGrade
from oopconcepts.teacher import Teacher

cc =  int(input('C Code : '))
cn = input('C Name : ')
ci = input('City : ')
rno = int(input('Roll no: '))
sn = (input('S name: '))
m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
eid = int(input('Eid : '))
tn = input('Teacher Name: ')
de = input('Dept name: ')
bp = float(input('basicpay : '))


# project = College(ccode=cc, cname=cn, ccity=ci)
#
# project.welcome_message(),
# project.display_college_details()

# project = Student(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn, m1=m1, m2=m2, m3=m3)

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn, m1=m1, m2=m2, m3=m3, )
project.welcome_message()
project.display_college_details()
print(f'Roll no: {project.rollno} \t Name: {project.studname} \n ' 
      f'Total: {project.calculate_total()}) \n Average: {project.calculate_average()}')

project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')

teach = Teacher(ccode=cc, cname=cn, ccity=ci, eid=eid, tn=tn, de=de, bp=bp)
print(f'Eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.de}')
print(f'Salary: {teach.calculate_salary()}'),