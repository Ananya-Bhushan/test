# Add controller functions here if needed
from app import app
from models.movie import Movie
from flask import jsonify, request

# @app.route('/v1/movie/<int:movie_id>', methods=['GET'])
# def get_movie(movie_id):
#     movie = Movie.query.get(movie_id)
#     print(2)
#     if movie:
#         return jsonify({
#             'id': movie.id,
#             'title': movie.title,
#             'poster_path': movie.poster_path,
#             'language': movie.language,
#             'overview': movie.overview,
#             'release_date': movie.release_date.isoformat()
#         })
#     else:
#         return jsonify({'error': 'Movie not found'}), 404

# @app.route('/v1/movie', methods=['POST'])
# def create_movie():
#     data = request.json
#     title = data.get('title')
#     poster_path = data.get('poster_path')
#     language = data.get('language')
#     overview = data.get('overview')
#     release_date = data.get('release_date')

#     if not title or not poster_path or not language or not overview or not release_date:
#         return jsonify({'error': 'Incomplete movie data provided'}), 400

#     movie = Movie(title=title, poster_path=poster_path, language=language, overview=overview, release_date=release_date)
#     app.db.session.add(movie)
#     app.db.session.commit()

#     return jsonify({'message': 'Movie created successfully'}), 201

# @app.route('/v1/movie/<int:movie_id>', methods=['PUT'])
# def update_movie(movie_id):
#     movie = Movie.query.get(movie_id)
#     if not movie:
#         return jsonify({'error': 'Movie not found'}), 404

#     data = request.json
#     title = data.get('title')
#     poster_path = data.get('poster_path')
#     language = data.get('language')
#     overview = data.get('overview')
#     release_date = data.get('release_date')

#     if title:
#         movie.title = title
#     if poster_path:
#         movie.poster_path = poster_path
#     if language:
#         movie.language = language
#     if overview:
#         movie.overview = overview
#     if release_date:
#         movie.release_date = release_date

#     app.db.session.commit()

#     return jsonify({'message': 'Movie updated successfully'})

# @app.route('/v1/movie/<int:movie_id>', methods=['DELETE'])
# def delete_movie(movie_id):
#     movie = Movie.query.get(movie_id)
#     if not movie:
#         return jsonify({'error': 'Movie not found'}), 404

#     app.db.session.delete(movie)
#     app.db.session.commit()

#     return jsonify({'message': 'Movie deleted successfully'})
