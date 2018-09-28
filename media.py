import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    # Triple quotes is for multi line documentation
    # class variable, one for the class. Constants are all caps
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        print("Movie.__init__ called")
        # title, storyline, poster_image_url, trailer_youtube_url are instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
        
    
