insert into platform (platform_name, platform_abbreviation)
values ('Playstation 5', 'PS5'),
        ('Playstation 4', 'PS4'),
        ('Xbox Series X | S', 'XSX'),
        ('Xbox One', 'XONE'),
        ('Nintendo Switch', 'Switch'),
        ('PC (Microsoft Windows)', 'PC')
ON DUPLICATE KEY UPDATE platform_name = VALUES(platform_name);