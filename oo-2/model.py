
class Movie:
    def __init__(self, name, year, duration):
        self.name = name
        self.year = year
        self.duration = duration


class Series:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons


avengers = Movie('Avengers - Infinity War', 2018, 160)
print(
    f'Nome: {avengers.name} - Ano: {avengers.year} - Duração: {avengers.duration}')

atlanta = Series('Atlanta', 2018, 2)
print(f'Nome: {atlanta.name} - Ano: {atlanta.year} - Duração: {atlanta.seasons}')
