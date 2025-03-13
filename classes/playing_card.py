from dataclasses import dataclass

@dataclass
class PlayingCard:
    suit: str
    rank: str

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"PlayingCard(suit={self.suit}, rank={self.rank})"
    

# Creating a few playing cards
card1 = PlayingCard("Hearts", "Ace")
card2 = PlayingCard("Spades", "7")