movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def check_score_greater(movie):
    if movie['imdb'] > 5.5:
        return True
    else:
        return False
#print(check_score_greater(movies[0]))
    

#2
def sublist_with_score_above():
    sublist = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            sublist.append(movie)
    return sublist
#print(sublist_with_score_above())


#3
def movies_under_that_category(category):
    category_movies = []
    for movie in movies:
        if movie['category'] == category:
            category_movies.append(movie)
    return category_movies

#print(movies_under_that_category('Suspense'))


#4
def average_imdb(movies):
    overall = 0
    for movie in movies:
        overall += float(movie['imdb'])
    averege = overall/int(len(movies))
    return averege

#print(average_imdb(movies[0:3]))


#5
def average_of_category(category):
    overall = 0
    count = 0
    for movie in movies:
        if movie['category'] == category:
            count += 1
            overall += float(movie['imdb'])
    average = overall / count
    return average

#print(average_of_category('Romance'))