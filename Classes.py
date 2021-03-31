class Greeting():

    def __init__(self, Word = None):
        self.__Word = Word

    def __repr__(self):
        return 'Greeting my friend ' + str(Word) + ' !'
