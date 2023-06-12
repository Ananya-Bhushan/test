# Add controller functions here if needed
from app import app
from models.movie import Movie
from flask import jsonify, request


@app.route('/v1/movie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        return jsonify({
            'id': movie.id,
            'title': movie.title,
            'poster_path': movie.poster_path,
            'language': movie.language,
            'overview': movie.overview,
            'release_date': movie.release_date.isoformat()
        })
    else:
        return jsonify({'error': 'Movie not found'}), 404


