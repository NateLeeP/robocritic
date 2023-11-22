CREATE TABLE `review` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `url` varchar(255),
  `robo_score` decimal(2,1),
  `reviewer_id` integer,
  `game_id` integer,
  `publisher_id` integer,
  `review_publish_date` date,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `publisher` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `publisher_name` varchar(255),
  `publisher_domain_name` varchar(255),
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `game` (
  `id` integer PRIMARY KEY,
  `title` varchar(255),
  `release_date` date,
  `created_at` timestamp
);

CREATE TABLE `reviewer` (
  `id` integer PRIMARY KEY,
  `reviewer_full_name` varchar(255),
  `publisher_id` int
);

CREATE TABLE `platform` (
  `id` integer PRIMARY KEY,
  `platform_name` varchar(255)
);

CREATE TABLE `platform_game` (
  `id` integer PRIMARY KEY,
  `platform_id` int,
  `game_id` int
);

CREATE TABLE `genre` (
  `id` integer PRIMARY KEY,
  `genre_name` varchar(255)
);

CREATE TABLE `genre_game` (
  `id` integer PRIMARY KEY,
  `genre_id` int,
  `game_id` int
);

CREATE TABLE `review_pro` (
  `id` integer PRIMARY KEY,
  `review_id` int,
  `text` varchar(255)
);

CREATE TABLE `review_con` (
  `id` integer PRIMARY KEY,
  `review_id` int,
  `text` varchar(255)
);
