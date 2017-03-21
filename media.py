import webbrowser # importing module for playing trailer
import fresh_tomatoes
class Movie():
     """This class provides a way to store movies."""
     VALID_USERS= ["G","PG","PG-13","R"]
     def __init__(self,movie_title,movie_story,image_poster,trailer_youtube):
         self.title  = movie_title
         self.storyline = movie_story
         self.poster_image_url = image_poster
         self.trailer_youtube_url = trailer_youtube

     def show_trailer(self):
         webbrowser.open(self.trailer_youtube_url)

toy_story = Movie("TOY STORY",
"a story of a boy who loves toy",
"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
 
avatar = Movie("AVATAR","a story of aliens",
"http://www.impawards.com/2009/posters/avatar.jpg",
"https://www.youtube.com/watch?v=rygE8qidvjM")
#print(avatar.storyline)
#avatar.show_trailer()

Shutter_Island = Movie("Shutter Island","U.S. marshal investigates the disappearance of a murderess",
"https://02thriller2013.files.wordpress.com/2013/02/shutter-island-movie-poster.jpg",
"https://www.youtube.com/watch?v=lhBTlYQcBC0")
#Shutter_Island.show_trailer()

catch_me_if_you_can = Movie("Catch Me If You Can", "The true story of Frank Abagnale Jr. who,successfully conned millions of dollars", 
"http://www.impawards.com/2002/posters/catch_me_if_you_can_ver2_xlg.jpg",
"https://www.youtube.com/watch?v=SosRcIMCr5g") 

The_Hangover = Movie("The Hangover", 
"Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing",
"http://www.impawards.com/2009/posters/hangover.jpg",
"https://www.youtube.com/watch?v=vhFVZsk3XEs")

movies =[toy_story,avatar,Shutter_Island,catch_me_if_you_can,The_Hangover]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_USERS)
