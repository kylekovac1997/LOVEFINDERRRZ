-- Drop the users table if it exists
DROP TABLE IF EXISTS users;

-- Create the users table
CREATE TABLE users (
  userid SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  username VARCHAR(255) UNIQUE NOT NULL,
  admin BOOLEAN NOT NULL DEFAULT FALSE,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  dateofbirth DATE NOT NULL,
  createdon TIMESTAMP NOT NULL DEFAULT NOW(),
  lastactive TIMESTAMP,
  mobile VARCHAR(255),
  gender VARCHAR(255),
  firstname VARCHAR(255),
  lastname VARCHAR(255)
);

-- Insert sample data
INSERT INTO users (email, password_hash, username, admin, active, dateofbirth, createdon, mobile, gender, firstname, lastname)
VALUES ('kyleKovac97@gmail.com', '$2a$08$dTCFzE4wgTbwaOWZleC6JOceGQANjwu7FbMzfqa74/dpz4g4EiS5O', 'kyle', true, false, '1997-05-01', '2023-05-04', null, 'male', 'Kyle', 'Kovac'),
       ('morty.smith@gmail.com', '$2a$08$xWOQEtqYKF5dXPXu/0ubAeJafLlWdAyBnDytpvIsbSjXtXeEOC2ka', 'Morty-Smith', false, true, '2005-08-12', '2023-05-04', null, 'male', 'Morty', 'Smith');
