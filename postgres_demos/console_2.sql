INSERT INTO owner(OWNER_NAME, OWNER_AGE)
VALUES ('Peter', 26),
       ('George', 32),
       ('Amy', 67);

INSERT INTO dog (owner_id, dog_age, dog_name)
VALUES (1, 2, 'Fluffy'),
       (3, 3, 'Bully'),
       (1, 5, 'Rousey');

INSERT INTO cat (cat_name, cat_age, owner_id)
VALUES ('Tommy', 1, 2),
       ('Jessy', 7, 3),
       ('Bubbles', 3, 2);

INSERT INTO hotel (hotel_name, hotel_stars)
VALUES ('Grand Pets Hotel', 5),
       ('Pets Heaven', 2);

INSERT INTO dog_room (register_date, unregister_date, hotel_id, dog_id)
VALUES ('2020-06-08', '2020-06-10', 1, 1),
       ('2020-06-10', '2020-06-15', 2, 2),
       ('2020-06-20', '2020-06-23', 2, 3);

INSERT INTO cat_room (register_date, unregister_date, hotel_id, cat_id)
VALUES ('2020-09-09', '2020-10-10', 1, 1);
