# section12-2

import sqlite3

# DB파일 조회 (없으면 새로 생성)
conn = sqlite3.connect('C:/python_class/pythonStudy/resource/database.db', isolation_level=None)

# 커서 바인딩
c = conn.cursor()

# 데이터 조회 (전체)
# c.execute("SELECT * FROM users")

# 커서 위차가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

print()

# 순회 1
rows = c.fetchall()
# for row in rows:
#     print('retrievel > ', row)

# 순회 2
# for row in c.fetchall():
#     print('retrieve > ', row)

# 순회 3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 > ', row)



print()
print()




# WHERE Retrieve
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1 ', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve 2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2 ', c.fetchone())
print('param2', c.fetchall())


# where 3 
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3 ', c.fetchone())
print('param3', c.fetchall())

# where4
param4 = (3, 5)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4 : ', c.fetchall())

# where5
c.execute('SELECT * FROM users WHERE id IN("%d", "%d")' % (3,4))
print('param5 : ', c.fetchall())

# where6
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2',{"id1":2, "id2":5})
print('param6 : ', c.fetchall())

# Dump 출력
with conn:
    with open('C:/python_class/pythonStudy/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')


# f.close()













