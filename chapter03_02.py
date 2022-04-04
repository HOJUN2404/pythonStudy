# Chapter03_02
# 파이썬 심화
# 시퀀스형
# 해시테이블( Hashtable ) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
print('ex1-1 :')
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print('ex1-2 :', hash(t1))
# print('ex1-3 :', hash(t2))

# 지능형 딕셔너리
import csv

# 외부 CSV TO List of tuple

with open('./resource/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('ex2-1',)
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('ex2-2',)
print(n_code1)

print()
print()

print('ex2-3',)
print(n_code2)

print()
print()
print()
print()
print()
print()
print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5')
)


new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('ex3-1 : ', new_dict1)



# Use setdefault -> 중복되는 key가 있으면 append 하겠다. 
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print('ex3-2 : ', new_dict2)


# 사용자 정의 dict 상속 (UesrDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called : __contains_')
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one':1, 'two':2})
user_dict3 = UserDict([('one',1), ('two',2)])



# 출력
print('ex4-1 :', user_dict1)
print('ex4-2 :', user_dict2)
print('ex4-3 :', user_dict3)

print('ex4-4', user_dict2.get('two'))
print('ex4-5', user_dict2.get('two2'))

print('ex4-6', 'one' in user_dict3)
print('ex4-6', user_dict3['three'])

print('ex4-7 :', 'three' in user_dict3)










    
    