import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title_year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    input_file = csv.DictReader(open(f"/tmp/{fname}"))
    for row in input_file:
        if not row["title_year"] == "" and int(row["title_year"]) >= 1960:
            #  if "title_year" in row and int(row["title_year"]) >= 1960 :
            movies[row["director_name"]].append(
                Movie(row["movie_title"], [row["title_year"], row["imdb_score"]])
            )

    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total = 0
    count = 0
    print(movies)
    for movie in movies:
        try: print(float(movie.score[1]))
        except TypeError:
            continue
        count = count + 1
        total = total + float(movie.score[1])
    return round((total/count), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    director_del = []
    for director in directors:
        if len(directors[director]) < 4:
            director_del.append(director)

    for dir in director_del:
        del directors[dir]

    returnValue = []

    # for director, movies in directors.items():
    #     total = 0
    #     count = 0
    #     for mov in movies:
    #         total = total + float(mov.score[1])
    #         count = count + 1
    #     returnValue.append((director, round((total / count), 1)))

    for director, movies in directors.items():
        returnValue.append(
            (
                director,
                round((sum([float(mov.score[1]) for mov in movies]) / len(movies)) , 1)
            )
        )

    return sorted(returnValue, key=lambda x: x[1], reverse=True)




director_movies = get_movies_by_director()
get_average_scores(director_movies)
print(director_movies['Peter Jackson'])
calc_mean_score(director_movies['Sergio Leone'])
print(director_movies.items())
