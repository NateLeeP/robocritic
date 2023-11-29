-- Set column type to int because foreign key constraint failing
-- when column type was 'unsigned'

ALTER TABLE game MODIFY id int;
ALTER TABLE genre modify id int;
ALTER TABLE genre_game modify id int;
ALTER TABLE platform modify id int;
ALTER TABLE platform_game modify id int;
ALTER TABLE publisher modify id int;
ALTER TABLE review modify id int;
ALTER TABLE review_con modify id int;
ALTER TABLE review_pro modify id int;