class AgeException(Exception):
    def __init__(self, errormsg):
        super().__init__(errormsg)
