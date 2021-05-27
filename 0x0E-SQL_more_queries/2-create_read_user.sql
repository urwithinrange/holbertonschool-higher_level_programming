-- script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS user_0d_2;
CREATE USER IF NOT EXIST 'user_0d_2'@localhost;
IDENTIFIED BY 'user_0d_2_pwd'
GRANT USAGE ON *.* IF NOT EXITSTS TO 'user_0d_2'@localhost;