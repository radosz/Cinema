show_all_movies_query = """SELECT * FROM Movies
ORDER BY rating DESC
"""
show_all_reservation = """SELECT * FROM Reservations
"""
cancel_reservation = """SELECT reservation_id as id,username,movies.name as movie,type,row,col FROM Reservations
JOIN projections
ON reservations.projection_id =projections.projection_id
JOIN movies
ON projections.movie_id = movies.movie_id
"""
show_username_reservation = """SELECT reservation_id FROM Reservations
WHERE username = ?
"""
movie_id_query = """SELECT movie_id FROM Movies WHERE name = ?
"""
projection_by_id_date = """SELECT movies.movie_id as id ,name as movie,rating,type,date,time
FROM Movies
JOIN projections ON movies.movie_id = projections.movie_id
WHERE  movies.movie_id = ? AND date LIKE ?
"""
projection_by_id_no_date = """SELECT projection_id as id ,name as movie,rating,type,date,time
FROM Movies
JOIN projections ON movies.movie_id = projections.movie_id
WHERE  movies.movie_id = ?
"""
reservation_query = """INSERT INTO reservations(username,projection_id,row,col)
VALUES(?,?,?,?)
"""
catalog_query = """SELECT projection_id as id,name,rating,type,date,time
FROM movies
JOIN projections ON projection_id = movies.movie_id
WHERE date = ?
"""
delete_reservation = """DELETE FROM reservations
WHERE reservation_id = ?
"""
projection_date = """SELECT date
FROM projections
WHERE projection_id=?
"""
movie_by_id = """SELECT name,rating
FROM movies
WHERE movie_id = ?
"""
projection = """SELECT projection_id as id ,name as movie,rating,type,date,time
FROM Movies
JOIN projections ON movies.movie_id = projections.movie_id
WHERE  projection_id = ?
"""
reservation_where_prj_id = """SELECT projection_id,row,col
FROM Reservations
WHERE projection_id = ?
"""
