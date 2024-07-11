CREATE DATABASE IF NOT EXISTS robocritic;
 
USE robocritic;

CREATE TABLE IF NOT EXISTS game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    art_url VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS platform (
    id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS platform_game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    platform_id INT NOT NULL, 
    game_id INT NOT NULL,
    FOREIGN KEY (platform_id) REFERENCES platform(id),
    FOREIGN KEY (game_id) REFERENCES game(id)
);

CREATE TABLE IF NOT EXISTS publisher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(50) NOT NULL,
    publisher_domain_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table IF NOT EXISTS reviewer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reviewer_full_name VARCHAR(100) NOT NULL,
    publisher_id INT NOT NULL,
    FOREIGN KEY (publisher_id) REFERENCES publisher(id)
);

create table IF NOT EXISTS review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_url VARCHAR(100) NOT NULL,
    robo_score DECIMAL(3, 1) NOT NULL,
    critic_score DECIMAL(3, 1) NOT NULL,
    reviewer_id INT NOT NULL,
    game_id INT NOT NULL,
    publisher_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reviewer_id) REFERENCES reviewer(id),
    FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (publisher_id) REFERENCES publisher(id)
);

create table IF NOT EXISTS review_con (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_id INT NOT NULL,
    cons VARCHAR(1000) NOT NULL,
    FOREIGN KEY (review_id) REFERENCES review(id)
);

create table IF NOT EXISTS review_pro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_id INT NOT NULL,
    pros VARCHAR(1000) NOT NULL,
    FOREIGN KEY (review_id) REFERENCES review(id)
);