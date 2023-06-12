# MVC
This project is about building a REST API using Flask,MySQL and MVC (Model-View-Controller) pattern. The API provides movie information based on the provided movie ID.

Tech Stack 1.Flask 2.MySQL 3.Python

controller This file represents the controller layer of MVC pattern.The controller layer is represented by MovieController used for retrieval logic of movie information based on the movie ID.

model  file represents all the user's data-retrieval related logic.It connects to mysql database retrieves movie information based on movie id.

view file represents all the records fetched within the model.Raw movie details obtained from the database is transformed into a standardized expected movie response dictionary.

migrations file used to manage changes to the database schema over time, such as creating or modifying tables, adding or removing columns, etc.

app file is responsible for creating the Flask application instance and configuring it.

API Definition

GET '/v1/movie/int:movie_id' HOST: : RESPONSE: { "id":<movie_id>, "title":<movie_name>, "poster_path":, "language":, "overview":<movie_description>, "release_date": }

OUTPUT When movie_id is valid

![outpu1](https://github.com/Ananya-Bhushan/test/assets/85629090/cb7b0e56-7eed-4a23-9fbb-34276fdca2e1)


When movie_id is invalid

![output2](https://github.com/Ananya-Bhushan/test/assets/85629090/5c03c459-0432-4981-95be-32ae07e4f232)

