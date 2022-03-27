# Section 12 
# SQLite 연동, 테이블 생성, 데이터 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDateTime = now.strftime('%y-%m-%d %H:%M:%S')
print("nowDateTime : ", nowDateTime)



print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)


# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/python_class/pythonStudy/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()

print('Cursor Type : ', type(c))


# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, \
# phone text, website TEXT, regdate TEXT)")

# Input Date to Table
c.execute("INSERT INTO users VALUES(1, 'kim', 'rlaghwns1995@naver.com', '010-6737-2404', 'hojunday.naver.com', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)",(2, 'park', 'park@daum.et', '010-1111-1111', 'par.com', nowDateTime))

# Many 삽입 (튜플, 리스트)
userList = ( \
    (3, 'Lee', 'lee@naver.com', '010-2222-2222', 'lee.com', nowDateTime),
    (4, 'cho', 'cho@naver.com', '010-3333-3333', 'cho.com', nowDateTime),
    (5, 'hwang', 'hwang@naver.com', '010-4444-4444', 'hwang.com', nowDateTime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")

# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영 (오토 커밋)
# 오토커밋 안했을 경우 conn.commit 명령어 실행하여 커밋 해주어야 한다. 
# 롤백 시킬 때에는 conn.rollback 처리 해주어야 한다. 

conn.close()


