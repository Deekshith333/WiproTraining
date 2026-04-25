class College:
    def __init__(self, ccode, cname, ccity):
        self.collcode = ccode
        self.collname = cname
        self.collcity = ccity

    def welcome_message(self):
        print('Hello there')

    def display_college_details(self):
        print('College Code : {self.collcode} \n '
              'College Name: {self.collcname} \n '
              'College City: {self.collcity}', self.collcode, self.collname, self.collcity)
