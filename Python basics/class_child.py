from class_demo import calculator

class child(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self,2,9)

    def multiply(self):
        return self.Firstnumber * self.Secondnumber * self.add()

obj = child()
print(obj.multiply())

