import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.title, toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alian planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()

matrix = media.Movie("Matrix",
                     "In a dystopia overrun by robots, Neo (Keanu Reeves), mankind's greatest hope, is trapped in a limbo world. Meanwhile, the majority of the planet's population remains in a state of suspended virtual reality. The few humans who are cognizant of the grim realities of the world desperately try to hold off their mechanical enemies long enough for Neo to escape and save the day, but things turn disastrous when all-powerful computer program Agent Smith (Hugo Weaving) arrives in the flesh.",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcSnqPZ_Ay9mOmXRylUQqzfahOLH_w7A19Qvhph82oeAL1nws_xL",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
#matrix.show_trailer()
                     
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

kali_linux = media.Movie("Kali Linux Tutorial",
                         "Learn to user Kali linux",
                         "https://www.kali.org/wp-content/uploads/2016/08/kali-rolling-2016-2-release3-350x284.png",
                         "https://www.youtube.com/watch?v=OcVE6rQ9_FU&list=PL4p9D8SidmadJPVQMV_P9723W0igGibVJ&index=2&t=5089s")

movies = [toy_story, avatar, matrix, school_of_rock, hunger_games, kali_linux]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(hunger_games.__dict__)
#print(hunger_games.__class__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
