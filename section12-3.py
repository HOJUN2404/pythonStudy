# section 12-3
# 파이썬 데이터베이스 연동 (SQLite)
# 데이터 테이블 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('C:/python_class/pythonStudy/resource/database.db', isolation_level=None)


c = conn.cursor()

# c.execute("UPDATE users SET username = ? WHERE id = ?", ("niceman", 2))

# c.execute("UPDATE users SET username = :name WHERE id = :id", {'name' : 'goodman', 'id' : 5})

# c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('badboy', 3))

# 중간데이터 확인1

# for user in c.execute("SELECT * FROM users"):
#     print(user)

# conn.commit()


c.execute("DELETE FROM users WHERE id = ?", (2,))   


c.execute("DELETE FROM users WHERE id = :id", {"id":5})

c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

print()


print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")


# 접속 해제
conn.close()







