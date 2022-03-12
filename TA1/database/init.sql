CREATE DATABASE ta1;
USE ta1;

CREATE TABLE Person (
  PersonID SERIAL PRIMARY KEY,
  Firstname NVARCHAR(500) NOT NULL,
  Lastname NVARCHAR(500) NOT NULL
);

ALTER user 'root' IDENTIFIED WITH mysql_native_password BY '';
flush privileges;
