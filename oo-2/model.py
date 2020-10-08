class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def do_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self._name} - {self.year}: {self._likes} Likes'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} min - {self._likes} Likes'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} seasons - {self._likes} Likes'
class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self.programs = programs

    def size(self):
        return len(self.programs)


avengers = Movie('Avengers - Infinity War', 2018, 160)
injustice = Movie('Injustice', 2021, 190)
atlanta = Series('Atlanta', 2018, 2)
the_flash = Series('The Flash', 2014, 5)

avengers.do_like()
injustice.do_like()
injustice.do_like()
atlanta.do_like()
atlanta.do_like()
the_flash.do_like()

movies_and_series = [avengers, injustice, atlanta, the_flash]
weekend_playlist = Playlist('Weekend', movies_and_series)

for program in weekend_playlist.programs:
    print(program)
