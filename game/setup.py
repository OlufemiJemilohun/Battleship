'''Setup the boards/ships for the game
'''

# Game 
from board import Board
from ships import Ships
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Linear algebra
import numpy as np
# Type hints
from typing import List, Dict

from random import randint

@dataclass
class Setup:
  '''Class contains setups the game for players one and two
  '''
  player1: Dict = field(default_factory=lambda: {})
  player2: Dict = field(default_factory=lambda: {})

  def __post_init__(self):
    '''Create boards/ships for the players
    '''
    for player in vars(self):
      vars(self)[player]['board'] = Board()
      vars(self)[player]['ships'] = Ships()

    def place_ships(board, ships):
      '''Randomly place the ships on the board for each player
      '''
      orientation = {
          1: 'horizontal',
          0: 'vertical'
      }
      print(orientation[randint(0, 1)])
      print(randint(0, 7), ships.carrier)
        
      pass
    
    place_ships(self.player1['board'], self.player1['ships'])
  
if __name__ == '__main__':
  S = Setup()
  #print(S.player1)
