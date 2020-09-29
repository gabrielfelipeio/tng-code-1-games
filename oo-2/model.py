
class Movie:
    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def do_like(self):
        self.likes += 1


class Series:
    def __init__(self, name, year, seasons):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def do_like(self):
        self.likes += 1


avengers = Movie('Avengers - Infinity War', 2018, 160)
print(
    f'Nome: {avengers.name} - Ano: {avengers.year} - Duração: {avengers.duration} - Likes: {avengers.likes}')

atlanta = Series('Atlanta', 2018, 2)
print(f'Nome: {atlanta.name} - Ano: {atlanta.year} - Duração: {atlanta.seasons} - Likes: {atlanta.likes}')
