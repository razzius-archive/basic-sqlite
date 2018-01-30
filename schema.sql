CREATE TABLE IF NOT EXISTS "users" (
    "pk" INTEGER PRIMARY KEY,
    "username" varchar(255) unique,
    "fav_color" varchar(255) DEFAULT NULL
);