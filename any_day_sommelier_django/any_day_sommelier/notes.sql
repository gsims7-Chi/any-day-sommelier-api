
-- DROP DATABASE IF EXISTS any_day_sommelier;
-- CREATE DATABASE any_day_sommelier;

-- \c any_day_sommelier

-- CREATE TABLE wine (
--   id SERIAL PRIMARY KEY,
--   type VARCHAR(32)
-- );

-- CREATE TABLE food (
--   id SERIAL PRIMARY KEY,
--   type VARCHAR(64),
--   example_1 VARCHAR(64),
--   example_2 VARCHAR(64)
-- );

-- CREATE TABLE user (
--   id SERIAL PRIMARY KEY,
--   email VARCHAR(64),
--   password VARCHAR(32)
-- );

-- CREATE TABLE pairing (
--   id SERIAL PRIMARY KEY,
--   wine_id INTEGER REFERENCES wine(id),
--   food_id INTEGER REFERENCES food(id)

-- );

-- CREATE TABLE favorites (
--   id SERIAL PRIMARY KEY,
--   user_id INTEGER REFERENCES user(id),
--   pairing_id INTEGER REFERENCES pairing(id)
-- );


INSERT INTO any_day_sommelier_wine
  (type)
  VALUES
  ('Riesling'),
  ('Pinot Gris'),
  ('Sauvignon Blanc'),
  ('Chardonnay'),
  ('Pinot Noir'),
  ('Zinfandel'),
  ('Syrah'),
  ('Cabernet Sauvignon'),
  ('Merlot'),
  ('Rose'),
  ('Malbec'),
  ('Moscato'),
  ('Champagne');

INSERT INTO any_day_sommelier_food
  (type, example_1, example_2)
  VALUES
  ('Red Meat', 'Beef', 'Lamb'),
  ('Pork', 'Pork Chop', 'Pork Tenderloin'),
  ('Poultry', 'Chicken', 'Duck'),
  ('Fish', 'Tuna', 'Cod'),
  ('Shellfish', 'Lobster', 'Crab'),
  ('Cured Meat', 'Salami', 'Proscuitto'),
  ('Mollusk', 'Oyster', 'Mussels'),
  ('Soft Cheese', 'Brie', 'Mascarpone'),
  ('Pungent Cheese', 'Bleu Cheese', 'Gorgonzola'),
  ('Hard Cheese', 'Cheddar', 'Asiago'),
  ('Fruit', 'Strawberry', 'Peach');

INSERT INTO any_day_sommelier_pairing
  (wine_id, food_id)
  VALUES
  (11, 1),
  (7, 1),
  (8, 1),
  (5, 6),
  (12, 6),
  (1, 6),
  (9, 2),
  (6, 2),
  (5, 3),
  (4, 3),
  (2, 4),
  (4, 4),
  (4, 5),
  (2, 5),
  (10, 5),
  (2, 7),
  (13, 7),
  (5, 8),
  (4, 8),
  (9, 9),
  (6, 9),
  (11, 10),
  (8, 10),
  (7, 10),
  (12, 11),
  (13, 11);




-- ROUTES------------------


-- /                 GET         index         Home
-- */pairing          GET         index         Index of all pairings
-- */wine/:id         GET         show          Show individual wine - and which entrees it goes with
-- */wine             GET         index         Index of all wines
-- */food/:id         GET         show          Show individual dish - and wines it goes with
-- */food             GET         index         Index all dishes
-- /auth             POST        create        Create new user
-- /auth/:id         GET         show          View user profile - including their liked pairings
-- /auth/:id         DELETE      destroy       Destroy account
-- /auth/:id/edit    PUT         update        update profile -- would this be for adding a pairing to favorites?
-- /upvote?
-- /downvote?
