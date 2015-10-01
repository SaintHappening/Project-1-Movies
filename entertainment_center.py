# Movies broken out individually, html page and media files imported
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"www.youtube.com/watch?v=KYz2wyBy3kc")	

plan_9 = media.Movie("Plan 9 from Outer Space",
						"Bela Lugosi's last movie",
						"https://upload.wikimedia.org/wikipedia/commons/b/bf/Plan_9_Alternative_poster.jpg",
						"https://www.youtube.com/watch?v=u2ukRYsYPmo")

heat = media.Movie("Heat",
						"A classic heist movie",
						"http://www.movie-poster-artwork-finder.com/posters/heat-1995-poster-artwork-al-pacino-robert-de-niro-val-kilmer.jpg",
						"https://www.youtube.com/watch?v=0xbBLJ1WGwQ")

dr_Strangelove = media.Movie("Dr Strangelove",
						"Gentlemen, you can't fight in here! This is the war room!",
						"http://ih0.redbubble.net/image.28674037.3399/flat,800x800,070,f.u1.jpg",
						"www.youtube.com/watch?v=IE9CmX15PYA")

inception = media.Movie("Inception",
						"Check your totem",
						"http://www.pxleyes.com/images/contests/minimalist-poster/fullsize/INCEPTION-4e11d1569945c_hires.jpg",
						"www.youtube.com/watch?v=66TuSJo4dZM")

casablanca = media.Movie("Casablanca",
						"Of all the gin joints in all the world",
						"https://www.movieposter.com/posters/archive/main/27/MPW-13851",
						"www.youtube.com/watch?v=EJvlGh_FgcI")

# Pop the list and webpage below
movies = [toy_story, plan_9, heat, dr_Strangelove, inception, casablanca]
fresh_tomatoes.open_movies_page(movies)	