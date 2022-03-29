# Chapter02_01
# 데이터 모델 (Data Model)
# 참조 : http://docs/python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 => 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# a = 7
# print(id(a), type(a), dir(a))

# 파이썬 -> 일관성



# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
from typing import NamedTuple

line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('EX1-1 -', line_leng1)

# Named 튜플 사용

from collections import namedtuple

# Named 튜플 선언
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX1-2 -', line_leng2)
print('EX1-3 -', line_leng1 == line_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False


# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)


print('EX2-2 - ', p1, p2, p3, p4, p5)

print()
print()






