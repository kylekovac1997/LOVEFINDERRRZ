-- psql
-- CREATE DATABASE LOVEFINDERRRZ;
-- \c LOVEFINDERRRZ
CREATE TABLE users (
    UserID SERIAL PRIMARY KEY,
    Email VARCHAR(255),
    Password_hash VARCHAR(255),
    UserName VARCHAR(255),
    Admin BOOLEAN,
    Active BOOLEAN,
    DataOfBirth VARCHAR(255),
    CreatedOn VARCHAR(255),
    LastActive INTEGER,
    Mobile INTEGER,
    Gender VARCHAR(255)
);
INSERT INTO users (Email, Password_hash, UserName, Admin, CreatedOn, DataOfBirth, Gender)
VALUES
('kyleKovac97@gmail.com', 'Admin', 'kyle', true, '2023-05-04', '1997-05-01', 'male'),
('morty.smith@gmail.com', 'password1', 'Morty-Smith', false, '2023-05-04', '2005-08-12', 'male');


