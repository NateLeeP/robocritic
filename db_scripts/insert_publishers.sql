  

INSERT INTO publisher (publisher_name, publisher_domain_name) 
VALUES ('PC Gamer', 'https://www.pcgamer.com/'),
         ('IGN', 'https://www.ign.com/')
ON DUPLICATE KEY UPDATE publisher_name = VALUES(publisher_name)