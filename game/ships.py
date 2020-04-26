'''Create the ships used in the game
'''

# Linear Algebra
import numpy as np
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hints
from typing import List, Dict

# Ship types and sizes
SHIP_SIZES = {
    'carrier': 5,
    'battleship': 4,
    'destroyer': 3,
    'submarine': 3,
    'patrol_boat': 2
}

@dataclass
class Ship:
  '''Create the 8x8 boards for one player
  '''
  carrier: np.array = None
  battleship: np.array = None
  destroyer: np.array = None
  submarine: np.array = None
  patrol_boat: np.array = None
  
  def __post_init__(self):
    '''Create current/previous board to track moves
    '''
    for ship in vars(self):
      vars(self)[ship] = np.zeros(shape=(
          SHIP_SIZES[ship]
      ))
  
if __name__ == '__main__':
  S = Ship()
  print(asdict(S))
