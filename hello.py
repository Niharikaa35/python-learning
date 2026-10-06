class VariableEX:
    name="niharika" #static variable

    @staticmethod
    def m1():
        print("I am static variable",VariableEX.name)

@staticmethod
def m2():
        print("accessing m1 method variable",VariableEX.name)

        VariableEX.m1()
        VariableEX.m2()

    
