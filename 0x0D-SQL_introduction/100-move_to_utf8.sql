-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unico
-- convert hbtn_0c_0, first_table, name 

USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
