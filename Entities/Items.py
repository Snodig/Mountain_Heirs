'''
 * File: Items.py
 * Date: 12-01-28
 *
 * Desc: All usable items (Does not include resources)
 *
 * Author: H. N. Skjevling
'''

from TheWorld import BaseEntity
from Utilities import Functions

class Item(BaseEntity):
  def __init__(self):
    BaseEntity.__init__(self, self.__class__.__name__)

class Tool(Item):
  pass

class Consumable(Item):
  pass

class Axe(Tool):
  pass

'''
_currentItemId = -1
def getNewItemId():
  global _currentItemId
  _currentItemId += 1
  return _currentItemId
'''

def initItemMap():
  Functions.registerItem(Axe())