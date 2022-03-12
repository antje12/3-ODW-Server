CREATE DATABASE fileSystemDB;
USE fileSystemDB;

CREATE TABLE File (
  fileid SERIAL PRIMARY KEY,
  filename NVARCHAR(100) UNIQUE NOT NULL,
  filesize INT,
  filecontent  NVARCHAR(500)
);

insert into File (filename, filesize, filecontent) values ('test_file', 1337, 'Hello world!');

ALTER user 'root' IDENTIFIED WITH mysql_native_password BY '';
flush privileges;
