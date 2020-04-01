class Card(object):

    def __init__(self, value, suit):
        self.__value = ''
        self.__suit = ''
        self.__color = ''
        self.__hardValue = ''
        self.__softValue = ''
        self.__visible = False
        self.__cardList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']

    def __str__(self):
        print(f'{self.__value}, {self.__suit}')

    def get_value(self):
        if self.__value not in self.__cardList:
            raise TypeError(f'{self.__value} not in cardList.')
        else:
            if self.__visible:
                return self.__value
            else:
                return 'unknown'

    def get_suit(self):
        if self.__suit not in ['s', 'd', 'c', 'h']:
            raise TypeError(f'{self.__suit} is not a valid suit.')
        else:
            return self.__suit

    def get_color(self):
        if self.__suit in ['d', 'h']:
            self.__color = 'red'
        else:
            self.__color = 'black'
        return self.__color

    def get_hardValue(self):
        if self.__visible:
            return self.__hardValue
        else:
            return 'unknown'

    def get_softValue(self):
        if self.__visible:
            return self.__softValue
        else:
            return 'unknown'

    def visible(self):
        return self.__visible

    def flip(self):
        if not self.__visible:
            self.__visible = True
        else:
            print('Card is already flipped.')
        return self.__visible
