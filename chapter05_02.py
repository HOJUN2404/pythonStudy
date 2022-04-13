# Chapter 06_02
# 파이썬 심화 - 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# Class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return(i for i in (self.__x, self.__y))  # Generator
    
    @property
    def x(self):
        print('Called Property X')
        return self.__x

    @x.setter
    def x(self, v):
        print('Called Property X Setter')
        self.__x = v

    @property
    def y(self):
        print('Called Property Y')
        return self.__y

    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError('30 Below is not possible')
        print('Called Property Y Setter')
        self.__y = v

# 객체 선언
v = VectorP(20, 30)

# print(v._x, v._y)
# print('ex1-1 :', v.__x, v.__y)

# v._y = 10
# print(v._x, v._y)

# Getter & Setter
v.x = 100

print('ex1-2 :', dir(v), v.__dict__)
print('ex1-3 :', v.x, v.y)

# Iter 확인
for val in v:
    print('ex1-2 :', val)

print()
print()


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()


print('ex2-1 :', use_slot)
# print('ex2-2 :', use_slot.__dict__)
print('ex2-1 :', no_slot)
print('ex2-2 :', no_slot.__dict__)

print()
print()


# 메모리 사용량 비교
import imp
from msilib.schema import RadioButton
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

# print(min(timeit.repeat(repeat_outer(use_slot), number=100000)))
# print(min(timeit.repeat(repeat_outer(no_slot), number=100000)))

print()
print()

# 객체 슬라이싱

class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjectS()

print('ex3-1 :', s.__dict__)
print('ex3-2 :', len(s))
print('ex3-3 :', len(s._numbers))
print('ex3-4 :', s[1:100])
print('ex3-5 :', s[-1])
print('ex3-6 :', s[::10])

print()
print()

# 파이썬추상클래스
# 

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스터스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것


# Sequence 상속 받지 않았지만, 자동으로 기능 작동
# 객체 전체를 자동으로 조사해서 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1, 50, 2)

i1 = IterTestA()

print('ex4-1 :', i1[4])
print('ex4-2 :', i1[4:10])
print('ex4-3 :', 3 in i1[1:10])

print()
print()


# Sequence 상속
# 요구사항인 추상메서드를 모두 구현해야 동작한다.

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])

i2 = IterTestB()
print('ex4-4 :', i2[4])
print('ex4-5 :', i2[4:10])
print('ex4-6 :', 3 in i2[1:10])

print()
print()
print()


import abc

class RandomMachine(abc.ABC): 

    # 추상메소드
    @abc.abstractclassmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''

    # 추상메소드
    @abc.abstractclassmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self):
        return self.pick()


# 서브클래스 확인
print('ex5-1 :', issubclass(RandomMachine, CraneMachine))
print('ex5-2 :', issubclass(CraneMachine, RandomMachine))


# 상속구조 확인
print('ex5-3 :', CraneMachine.__mro__)

cm = CraneMachine(range(1, 100))

print('ex5-4 :', cm._items)
print('ex5-5 :', cm.pick())

# Callable 됐는지 확인
print('ex5-5 :', cm())
print('ex5-5 :', cm.inspect())


















