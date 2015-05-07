PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Movies
(movie_id INTEGER PRIMARY KEY,
    name TEXT,
    rating FLOAT
);
INSERT INTO "Movies" VALUES(1,'The Hunger Games: Catching Fire',7.9);
INSERT INTO "Movies" VALUES(2,'Wreck-It Ralph',7.8);
INSERT INTO "Movies" VALUES(3,'Her',8.3);
CREATE TABLE Reservations
(reservation_id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY(projection_id) REFERENCES Projections(projection_id)
);
CREATE TABLE Projections
(projection_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date DATE,
    time TIME,
    FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);
INSERT INTO "Projections" VALUES(1,1,'3D','2014-04-01','19:10');
INSERT INTO "Projections" VALUES(2,1,'2D','2014-04-01','19:00');
INSERT INTO "Projections" VALUES(3,1,'4DX','2014-04-02','21:00');
INSERT INTO "Projections" VALUES(4,3,'2D','2014-04-05','20:20');
INSERT INTO "Projections" VALUES(5,2,'3D','2014-04-02','22:00');
INSERT INTO "Projections" VALUES(6,2,'2D','2014-04-02','19:30');
COMMIT;
