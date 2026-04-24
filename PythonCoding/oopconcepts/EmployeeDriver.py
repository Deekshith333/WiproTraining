from oopconcepts.EmployeeDetails import EmployeeDetails

#driver
eno = int(input('Emp no : '))
name =  input('Emp name : ')
bp = float(input('basic pay : '))

employee = EmployeeDetails(empno=eno, ename=name, basicpay=bp)
print('Employee number : ', employee.empno)
print('Employee name : ', employee.ename)
print('Basic Pay : ', employee.basic_pay)
print('Salary : ', employee.calculate_netsal())