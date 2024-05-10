'create a users table'
CREATE TABLE IF NOT EXIST users (
    id INT PRIMARY_KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL Unique,
    name VARCHAR(255));
    