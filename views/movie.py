from flask import jsonify
#from models.movie import Movie
from flask import Blueprint

movie_api = Blueprint('movie_api', __name__)

@movie_api.route('/v1/movie/<int:movie_id>', methods=['GET'])
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
