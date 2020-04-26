'''This script is used to create the boards for the game
'''

# Linear Algebra
import numpy as np
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hints
from typing import List, Dict

@dataclass
class Board:
  '''Create the 8x8 boards for one player
  '''
  current: np.array = None
  previous: np.array = None
  
  def __post_init__(self):
    '''Create current/previous board to track moves
    '''
    for board in vars(self):
      vars(self)[board] = np.zeros(shape=(8,8))

  
if __name__ == '__main__':
  B = Board()
  print(asdict(B))
