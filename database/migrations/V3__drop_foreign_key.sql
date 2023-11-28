ALTER TABLE genre_game DROP FOREIGN KEY genre_game_ibfk_1;
ALTER TABLE genre_game DROP FOREIGN KEY genre_game_ibfk_2;

ALTER TABLE platform_game DROP FOREIGN KEY platform_game_ibfk_1;
ALTER TABLE platform_game DROP FOREIGN KEY platform_game_ibfk_2;

ALTER TABLE review DROP FOREIGN KEY review_ibfk_2;
ALTER TABLE review DROP FOREIGN KEY review_ibfk_3;

ALTER TABLE review_con DROP FOREIGN KEY review_con_ibfk_1;

ALTER TABLE reviewer DROP FOREIGN KEY reviewer_ibfk_1;

ALTER TABLE review_pro DROP FOREIGN KEY review_pro_ibfk_1;
