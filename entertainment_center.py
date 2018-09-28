# Vocabulary
# class
# instance
# constructor
# self
# instance variable
# instance method

import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "Marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=6ziBFh3V1aM")
print(avatar.storyline)
#avatar.show_trailer()

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
