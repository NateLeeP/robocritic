ALTER TABLE `review` ADD FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`);

ALTER TABLE `review` ADD FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);

ALTER TABLE `review` ADD FOREIGN KEY (`reviewer_id`) REFERENCES `reviewer` (`id`);

ALTER TABLE `reviewer` ADD FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`);

ALTER TABLE `platform_game` ADD FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);

ALTER TABLE `platform_game` ADD FOREIGN KEY (`platform_id`) REFERENCES `platform` (`id`);

ALTER TABLE `genre_game` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`);

ALTER TABLE `genre_game` ADD FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);

ALTER TABLE `review_con` ADD FOREIGN KEY (`review_id`) REFERENCES `review` (`id`);

ALTER TABLE `review_pro` ADD FOREIGN KEY (`review_id`) REFERENCES `review` (`id`);
