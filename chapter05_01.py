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


# 증명
tl1.append(1000)
tl1[1].remove(105)

print('ex4-5 :', tl1)
print('ex4-6 :', tl2)
print('ex4-7 :', tl3)

print()
print()

print(id(tl1[2]))

tl1[1] += [110, 120]

# tuple을 수정할 경우에는 주소값이 재할당된다.
# tl1[2] += (110, 120)

print('ex4-8 :', tl1)
print('ex4-9 :', tl2)
print('ex4-10 :', tl3)

print(id(tl1[2]))

print()
print()
print()

# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('id(basket1) = ', id(basket1))
print('id(basket2) = ', id(basket2))
print('id(basket3) = ', id(basket3))

print()

print('id(basket1._products) = ', id(basket1._products))
print('id(basket2._products) = ', id(basket2._products))
print('id(basket3._products) = ', id(basket3._products))

print()
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('ex5-3 : ', basket1._products)
print('ex5-4 : ', basket2._products)
print('ex5-5 : ', basket3._products)

print()
print()
print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y 
    return x

x = 10
y = 5

print('ex6-1 :', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

print('ex 6-2 : ', mul(a,b), a, b)  # 가변형인 리스트 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)

print('ex 6-3 : ', mul(c,d), c, d)  # 불변형인 튜플이므로 원본데이터가 변경되지 않음


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('ex7-1 : ', tt1 is tt2, id(tt1), id(tt2)) 
print('ex7-2 : ', tt3 is tt1, id(tt3), id(tt1))

# 즉, str bytes frozenset Tuple 은 아무렇게나 복사하고 할당해도 사본을 생성하지 않기 때문에 마음 놓고 사용 가능



print()
print()
print()

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('ex 7-3 : ', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('ex 7-4 : ', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))


















