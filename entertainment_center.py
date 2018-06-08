import media
import fresh_tomatoes

Movie_1 = media.movie("Batman", "https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png",
                      "https://www.youtube.com/watch?v=neY2xVmOfUM")

Movie_2 = media.movie("Superman man of steel", "https://images7.alphacoders.com/413/thumb-1920-413789.jpg",
                      "https://www.youtube.com/watch?v=T6DJcgm3wNY")


Movie_3 = media.movie("avengers infinity wars", "https://wallpapercave.com/wp/wp2302349.png",
                      "https://www.youtube.com/watch?v=6ZfuNTqbHE8")


# list of movies
MyMovies = [Movie_1, Movie_2, Movie_3]

# calling method to open movies webpage
fresh_tomatoes.open_movies_page(MyMovies)
