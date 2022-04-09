# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

from re import X


print('EX1-1 :')
print(dir())
print()
print(__name__)

# ID vs __eq__ (==) 증명
x = {'name': 'kim', 'age':33, 'city':'incheon'}
y = X

print('ex2-1 :', id(x), id(y))
print('ex2-2 :', x == y)
print('ex2-3 :', x is y)
print('ex2-4 :', x, y)

x['class'] = 10
print('ex2-5 :', x, y)

print()
print()

z = {'name': 'kim', 'age':33, 'city':'incheon', 'class': 10}

print('ex2-6 :', x, z)
# 같은 객체인지 확인
print('ex2-7 :', x is z)
print('ex2-8 :', x is not z)
# 값이 같은지 확인
print('ex2-9 :', x == z)

# 객체 생성 후 완전불변 -> id는 객체주소(정체성)비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('ex3-1 :', id(tuple1), id(tuple2))
print('ex3-2 :', tuple1 is tuple2)
print('ex3-3 :', tuple1 == tuple2)
print('ex3-4 :', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy (얕은복사, 깊은복사)

# Copy 얕은복사 ??? 
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

#  ==은 값이 같은지 비교하는 것
#  is는 주소값이 같은지 비교하는 것.
print('ex4-1 :', tl1 == tl2)
print('ex4-2 :', tl1 is tl2)
print('ex4-1 :', tl1 == tl3)
print('ex4-1 :', tl1 is tl3)





















