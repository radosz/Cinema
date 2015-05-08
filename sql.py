show_all_movies_query = """SELECT * FROM Movies
ORDER BY rating DESC
"""
show_all_reservation = """SELECT * FROM Reservations
"""
movie_id_query = """SELECT movie_id FROM Movies WHERE name = ?
"""
projection_by_id_date = """SELECT movies.movie_id as id ,name as movie,rating,type,date,time
FROM Movies
JOIN projections ON movies.movie_id = projections.movie_id
WHERE  movies.movie_id = ? AND date LIKE ?
"""
projection_by_id_no_date = """SELECT movies.movie_id as id ,name as movie,rating,type,date,time
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
