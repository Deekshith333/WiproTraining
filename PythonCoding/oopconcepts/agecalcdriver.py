from oopconcepts.agecalc import AgeCalculation
from oopconcepts.myexception import AgeException

age = int(input('Age: '))

ageobj = AgeCalculation()

try:
    ageobj.voting_age_check(age)
    ageobj.pension_age_check(age)
    # if ageobj.voting_age_check(age):
    #     print('Eligible, Contact next step...')
except AgeException as ae:
    print(ae)
else:
    print("Eligible: contact next step")
