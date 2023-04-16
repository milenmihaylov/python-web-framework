SELECT cr.cat_id, h.hotel_name
FROM hotel h
JOIN cat_room cr on h.hotel_id = cr.hotel_id
WHERE h.hotel_id = 2;