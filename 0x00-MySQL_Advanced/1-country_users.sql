-- creates table user in any database
-- create table user with columns id, email, name and country
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM ('US', 'CO', 'TN') DEFAULT 'US',
	PRIMARY KEY (id)
);
