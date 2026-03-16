from event_bus import EventBus

# Initialize the global event bus.
bus = EventBus()


class MouseClickEvent:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class GameOver:
   
    def __init__(self, was_tie: bool = True, winner: str = None):
        self.was_tie = was_tie
        self.winner = winner


class PiecePlaceEvent:

    def __init__(self, side: str):
        self.side = side