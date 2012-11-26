#!/usr/bin/env python
#To launch: python fileName.py

# Define class here
class MyClass(object):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def set_var1 (self, var2):
        self.var1 = var1
    def set_var2(self, var2):
        self.var2 = var2
    def DoSomething (self, var3):
        print "+++ Printing object default values var1=%s, var2=%s and custom value var3=%s" % (self.var1, self.var2, var3)

if __name__ == '__main__':
    test = MyClass('Liverpool', 'FC')
    test.DoSomething('REDS')
