import mymodule

b = 100

class C1:
    def __init__(self):
        self.a = 1

def set(num):
    mymodule.a = num
    global b
    b = 10
    print mymodule.a, b

c = C1()
mydic = {type:123, type:12312}
print mydic
