CREATE DATABASE test ENCODING 'UTF8' OWNER student;
CREATE table dancers(id serial, name text);
GRANT ALL PRIVILEGES ON dancers to "www-data";

INSERT into dancers(name) values ('Lyle Beniga');
INSERT into dancers(name) values ('Anthony Lee');
INSERT into dancers(name) values ('Vinh Nguyen');
