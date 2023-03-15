-- script that creates the database and the user.
-- Query that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT CREATE ON hbtn_0d_2 TO 'user_0d_2'@'localhost';