""" Module doc string"""
class Card:   # inherits from object
    """Class doc string"""
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):  # getter property (creates rank.setter)
        """property doc"""
        return self._rank

    @rank.setter
    def rank(self, new_rank):  # setter property
        if isinstance(new_rank, str):
            self._rank = new_rank
        else:
            raise TypeError("rank must be a str")
        
    @property
    def suit(self):
        return self._suit

    def __str__(self):   # human-friendly
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # code-friendly
        return f"Card('{self.rank}', '{self.suit}')"


if __name__ == "__main__":
    # not executed when this file is imported
    c1 = Card('9', 'Diamonds')
#    print(f"{c1._rank = }")   # very naughty
    print(f"{c1.rank = }")   # not naughty
    print(f"{c1.suit = }")
    
    # print(f"{c1.get_rank() = }")
    c1.rank = '2'   # calls the setter property

    print(c1)  #  print(str(c1))   Card.__str__(c1)
    print(repr(c1))
    print(f"{c1 = }")
    
    