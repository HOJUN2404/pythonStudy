# http://docs.python.org/3/reference/datamodel.html#special-method-names
# https://www.tutorialsteacher.com/python/magic-methods-in-python

# 클래스 예제2 

class Vector(object):
    def __init__(self, *args):
        '''Create a vector, example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns thi vector information'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        '''Returns the vector addition of self and other'''
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(3,5)
v2 = Vector(15,20)
v3 = Vector()

# MagicMethod 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3)
print('EX3-5 - ', v1.__add__(v2))
# print('EX3-6 -', v1*v2)
# print('EX3-7 -', v1*10)
print('EX3-8 -', bool(v1), bool(v2))
print('EX3-9 -', bool(v3))

print()
print()





