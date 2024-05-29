class Song:
    count = 0
    genres = []
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
    
    @classmethod
    def add_song_to_count(cls,increment = 1):
        cls.count += increment
    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre)


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

print(ninety_nine_problems.name)
