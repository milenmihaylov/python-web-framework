SELECT cat.cat_id , cat_name, cat_age, owner_id, hotel_name FROM cat
JOIN cat_room cr on cat.cat_id = cr.cat_id
JOIN hotel h on cr.hotel_id = h.hotel_id
WHERE h.hotel_id = 2;