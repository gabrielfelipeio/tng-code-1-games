class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def do_like(self):
        self.likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('Avengers - Infinity War', 2018, 160)
avengers.do_like()
print(
    f'{avengers.name} - {avengers.duration}: {avengers.likes}')

atlanta = Series('Atlanta', 2018, 2)
atlanta.do_like()
atlanta.do_like()
print(f'{atlanta.name} - {atlanta.seasons}: {atlanta.likes}')
