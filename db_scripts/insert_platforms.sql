alter table platform auto_increment = 1;
insert into platform (platform_name, platform_abbreviation)
values ('PlayStation 5', 'PS5'),
        ('PlayStation 4', 'PS4'),
        ('Xbox Series X|S', 'XSX'),
        ('Xbox One', 'XONE'),
        ('Nintendo Switch', 'Switch'),
        ('PC (Microsoft Windows)', 'PC')
ON DUPLICATE KEY UPDATE platform_name = VALUES(platform_name);