-- psql
-- CREATE DATABASE LOVEFINDERRRZ;
-- \c LOVEFINDERRRZ
CREATE TABLE users (
    UserID SERIAL PRIMARY KEY,
    Email VARCHAR(255),
    Password VARCHAR(255),
    UserName VARCHAR(255),
    Admin BOOLEAN,
    Active BOOLEAN,
    DataOfBirth VARCHAR(255),
    CreatedOn VARCHAR(255),
    LastActive INTEGER,
    Mobile INTEGER,
    Gender VARCHAR(255),
    Interest VARCHAR(255)
);
INSERT INTO users (Email, Password, UserName, Admin) 
VALUES 
('kyleKovac97@gmail.com', 'Admin', 'kyle', 'true'),
('morty.smith@gmail.com', 'password1', 'Morty-Smith', 'false')

