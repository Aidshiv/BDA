import csv
from functools import reduce

def mapper(tags):
    key_value_pairs = []
    for row in tags:
        movie_id = row['movieId']
        tag = row['tag']
        key_value_pairs.append((movie_id, tag))
    return key_value_pairs

def reducer(key, values):
    return list(set(values))

def map_reduce(tags):
    key_value_pairs = mapper(tags)
    grouped_values = {}
    for key, value in key_value_pairs:
        if key not in grouped_values:
            grouped_values[key] = []
        grouped_values[key].append(value)
    result = {}
    for key in grouped_values:
        result[key] = reducer(key, grouped_values[key])
    return result

def load_tags(file_path):
    tags = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tags.append(row)
    return tags

def load_movies(file_path):
    movies = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies[row['movieId']] = row['title']
    return movies

tags = load_tags('tags.csv')
movies = load_movies('movies.csv')
result = map_reduce(tags)

for movie_id, tags in result.items():
    movie_title = movies[movie_id]
    print(f'Movie: {movie_title}, Tags: {", ".join(tags)}')
