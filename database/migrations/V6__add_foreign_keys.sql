ALTER TABLE genre_game
ADD CONSTRAINT FK_GenreGame_Game
FOREIGN KEY (game_id) REFERENCES game(id);

ALTER TABLE genre_game
ADD CONSTRAINT FK_GenreGame_Genre
FOREIGN KEY (genre_id) REFERENCES genre(id);

ALTER TABLE platform_game
ADD CONSTRAINT FK_PlatformGame_Game
FOREIGN KEY (game_id) REFERENCES game(id);

ALTER TABLE platform_game
ADD CONSTRAINT FK_PlatformGame_Platform
FOREIGN KEY (platform_id) REFERENCES platform(id);

ALTER TABLE review
ADD CONSTRAINT FK_Review_Game
FOREIGN KEY (game_id) REFERENCES game(id);

ALTER TABLE review_con
ADD CONSTRAINT FK_ReviewCon_Review
FOREIGN KEY (review_id) REFERENCES review(id);

ALTER TABLE review_pro
ADD CONSTRAINT FK_ReviewPro_Review
FOREIGN KEY (review_id) REFERENCES review(id);