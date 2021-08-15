x = 10
class Test:
    x = 20
    def func1(self):
        x = 30
    def func2(self):
        self.x = 30
    def prtx1(self):
        print(self.x)
    def prtx2(self):
        print(x)
obj1 = Test()
obj1.prtx1()#
obj1.func1()
obj1.prtx1()#
obj1.func2()
obj1.prtx2()#
print(obj1.x)#