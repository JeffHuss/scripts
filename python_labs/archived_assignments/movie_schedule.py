current_movies = {'The Grinch' : ['11:00am', '12:55pm', '2:30pm'],
                  'Rudolph' : ['11:05am', '1:10pm', '3:00pm'],
                  'Frosty the Snowman' : ['11:00am', '12:30pm', '2:00pm'],
                  'Christmas Vacation' : ['11:25am', '1:35pm', '4:30pm']}

# print('We\'re showing the following movies:')
# for i in current_movies:
#     print(i)

# movie = input('What movie would you like the showtime for?\n')
# showtime = current_movies.get(movie)

# if showtime == None:
#     print('Requested movie isn\'t playing.\n')
# else:
#     print(movie, 'is playing at', showtime)

for movie, showtime in current_movies.items():
    print(f"Movie: {movie}\nShowtimes: {showtime}\n")