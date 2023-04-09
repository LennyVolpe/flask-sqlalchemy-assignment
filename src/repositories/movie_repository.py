from src.models import db, movie


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        all_movies = movie.query.all()
        return all_movies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return movie.query.get(movie_id)

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        created_movie = movie(title=title, director=director, rating=rating)

        db.session.add(created_movie)
        db.session.commit()

        return created_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movies_by_title = movie.query.filter(
            movie.title.ilike(f"%{title}%")).all()
        return movies_by_title


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
