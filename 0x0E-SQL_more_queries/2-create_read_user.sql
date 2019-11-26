
-- Create DATABASE hbtn_0d_2
CREATE DATABASE hbtn_0d_2;
-- add user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhosts IDENTIFIED BY 'user_0d_2_pwd';
-- Give privileges
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhosts` IDENTIFIED BY 'User_0d_2_pwd';
-- Reload privileges
FLUSH PRIVILEGES;
