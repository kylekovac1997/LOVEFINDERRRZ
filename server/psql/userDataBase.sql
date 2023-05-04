-- psql
-- CREATE DATABASE LOVEFINDERRRZ;
-- \c LOVEFINDERRRZ
CREATE TABLE users (
    UserID SERIAL PRIMARY KEY,
    Email VARCHAR(255),
    Password VARCHAR(255),
    UserName VARCHAR(255)
);
INSERT INTO users (Email, Password, UserName) 
VALUES 
('kyleKovac97@gmail.com', 'AdminLOVERFINDERRZ0423810756', 'kyle'),
('morty.smith@gmail.com', 'password1', 'Morty-Smith'),
('rick.sanchez@yahoo.com', 'password2', 'Rick-Sanchez'),
('summer.smith@hotmail.com', 'password3', 'Summer-Smith'),
('jerry.smith@gmail.com', 'password4', 'Jerry-Smith'),
('beth.smith@gmail.com', 'password5', 'Beth-Smith'),
('birdperson@gmail.com', 'password6', 'Birdperson'),
('squanchy@gmail.com', 'password7', 'Squanchy');
