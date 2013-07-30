
import copy

a = [[1, 2, 3], [4, 5, 6], 4, 5, 6]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
e = a[-1::-1]
a.append(15)
a[-1] = 123
a[1][2] = 10
c[0][1] = 100
print a
print b
print c
print d
print 'e', e

dic={(1,2,3):[1,2,3], '2':'456'}
llll = dic[(1,2,3)]
llll.append(4)
print type(dic)
sett = set(['1,2,3','1,23'])
new = (12,23)
sett.add(new)

class ca(object):
    def name(self):
        self.arrr = 1
        self.liii = [1,2,3]
cccc = ca()
cccc.arrr = 2
bbbb = ca()

print ca.__dict__
 
