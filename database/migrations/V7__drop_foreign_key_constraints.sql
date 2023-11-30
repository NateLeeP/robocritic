ALTER TABLE genre_game
DROP CONSTRAINT FK_GenreGame_Game;

ALTER TABLE genre_game
DROP CONSTRAINT FK_GenreGame_Genre;

ALTER TABLE platform_game
DROP CONSTRAINT FK_PlatformGame_Game;

ALTER TABLE platform_game
DROP CONSTRAINT FK_PlatformGame_Platform;

ALTER TABLE review
DROP CONSTRAINT FK_Review_Game;
