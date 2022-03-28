# Chapter01-3
# 파이썬 심화 [ 10. Class & Method - 10. Class, Instance, Static Method -3 ]
# Class Method, Instance Method

class Student(object):
    '''
    Student Class
    Author : KIM HOJUN
    Date : 2022.03.28
    Description : Class, Static, Instance Method
    '''

    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{}{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {},{},{},{},{},{}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> ID :{}, fee :{}'.format(self._id, self._tuition * Student.tuition_per)

    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('Succed tuition increased')





student1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student2 = Student(2, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)

print(student1.__dict__)

# 기본정보
print(student1)
print(student2)

# 전체정보
print(student1.detail_info())
print(student2.detail_info())

# 학비 정보 (인상 전)
print(student1.get_fee())
print(student2.get_fee())

print()

# 학비 인상
# Student.tuition_per = 1.5

# Usecase Class Method
Student.raise_fee(1.5)

# 학비 정보(인상 후)
print(student1.get_fee_culc())
print(student2.get_fee_culc())



