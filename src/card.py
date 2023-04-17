class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    @property
    def value(self):
        try:
            value = int(self.rank)
        except:
            if self.rank == "A":
                value = 11
            else:
                value = 10
        return value    