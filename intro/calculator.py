class Calculator:


    def add(self,a ,b, c = None):
        if c is not None:
            return a + b + c
        else:
            return a+b
