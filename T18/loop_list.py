#************************ OPTIONAL BONUS TASK *******************
# define a list of strings of your 5 fave movies
# Loop over the list for each item in the list print out "Movie"
# Plus the movies name 
#****************************************************************

#---------------- Variables ------------------
movies = ["Avengers Infinity War","Batman Darkknight", "Fight Club","Memento" ]

#-------------------------
# For loop that prints out list of movies 
#-------------------------
for movie in movies:
    print(f"Movie: {movie}")

#---------------------------------
# Loop that prints out Movie1:<Movie 1's name> Movie 2: etc
#---------------------------------
print() # To add space in consol
for movie in movies:
    print(f"Movie{movies.index(movie) +1}:{movie}")
