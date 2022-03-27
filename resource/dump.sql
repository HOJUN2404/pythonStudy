BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone text, website TEXT, regdate TEXT);
INSERT INTO "users" VALUES(1,'kim','rlaghwns1995@naver.com','010-6737-2404','hojunday.naver.com','22-03-27 20:08:47');
INSERT INTO "users" VALUES(2,'park','park@daum.et','010-1111-1111','par.com','22-03-27 20:08:47');
INSERT INTO "users" VALUES(3,'Lee','lee@naver.com','010-2222-2222','lee.com','22-03-27 20:08:47');
INSERT INTO "users" VALUES(4,'cho','cho@naver.com','010-3333-3333','cho.com','22-03-27 20:08:47');
INSERT INTO "users" VALUES(5,'hwang','hwang@naver.com','010-4444-4444','hwang.com','22-03-27 20:08:47');
COMMIT;
