
class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def do_like(self):
        self.likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def do_like(self):
        self.likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


avengers = Movie('Avengers - Infinity War', 2018, 160)
print(
    f'Nome: {avengers.name} - Ano: {avengers.year} - Duração: {avengers.duration} - Likes: {avengers.likes}')

atlanta = Series('Atlanta', 2018, 2)
print(f'Nome: {atlanta.name} - Ano: {atlanta.year} - Duração: {atlanta.seasons} - Likes: {atlanta.likes}')
