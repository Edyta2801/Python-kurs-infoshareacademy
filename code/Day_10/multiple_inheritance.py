class UltimateBase(object):
    def check(self):
        print('base check')


class AMixin1(UltimateBase):
    def check(self):
        print('check A')


class BMixin1(UltimateBase):
    def check(self):
        print('check B')


class CMixin1(UltimateBase):
    def check(self):
        print('check C')


class AMixin2(UltimateBase):
    def check(self):
        print('check A')
        return super(AMixin2, self).check()


class BMixin2(UltimateBase):
    def check(self):
        print('check B')
        return super(BMixin2, self).check()


class CMixin2(UltimateBase):
    def check(self):
        print('check C')
        return super(CMixin2, self).check()


class MyView1(AMixin1, BMixin1, CMixin1):
    pass


class MyView2(AMixin2, BMixin2, CMixin2):
    pass


class MyView3(AMixin1, BMixin2, CMixin2):
    pass


class MyView4(AMixin2, BMixin1, CMixin2):
    pass


class MyView5(AMixin2, BMixin2, CMixin1):
    pass


class MyView6(AMixin1, BMixin1, CMixin2):
    pass


class MyView7(AMixin1, BMixin2, CMixin1):
    pass


class MyView8(AMixin2, BMixin1, CMixin1):
    pass


myview1 = MyView1()
myview2 = MyView2()
myview3 = MyView3()
myview4 = MyView4()
myview5 = MyView5()
myview6 = MyView6()
myview7 = MyView7()
myview8 = MyView8()

print("myview1.check()")
myview1.check()
print('------------------------')

print("myview2.check()")
myview2.check()
print('------------------------')

print("myview3.check()")
myview3.check()
print('------------------------')

print("myview4.check()")
myview4.check()
print('------------------------')

print("myview5.check()")
myview5.check()
print('------------------------')

print("myview6.check()")
myview6.check()
print('------------------------')

print("myview7.check()")
myview7.check()
print('------------------------')

print("myview8.check()")
myview8.check()
print('------------------------')
