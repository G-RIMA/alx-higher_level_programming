-- Creates a database hbtn_0d_usa and a table called states
-- the table states  has a unique,auto generated and cant be null id and a name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
     id INT AUTO_INCREMENT NOT NULL UNIQUE,
     name VARCHAR(256) NOT NULL,
     PRIMARY KEY(id)
);
