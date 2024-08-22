-- This SQL script creates a table users
-- Users table attributes are id, email, name and country
-- The enumeration of countries: US, CO and TN, never null default and
-- US will be first element.
CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(255) NOT NULL UNIQUE,
        name varchar(255),
	country varchar(2) NOT NULL DEFAULT 'US',
	CHECK (country IN ('US', 'CO', 'TN')));
