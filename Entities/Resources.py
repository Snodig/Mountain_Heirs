'''
 * File: Resources.py
 * Date: 12-02-27
 *
 * Desc: Resources, trade commodities, materials etc
 *
 * Author: H. N. Skjevling
'''

from TheWorld import BaseEntity
from Utilities import Functions

class ResourceNode(BaseEntity):
  def __init__(self, name, resourceName, amount=1):
    BaseEntity.__init__(self, name)
    self._amount = amount
    self._type = resourceName

class Resource(BaseEntity): 
  def __init__(self, name, value, weight):
    BaseEntity.__init__(self, name)
    self._value = value
    self._weight = weight

class Food(Resource):
  def __init__(self):
    Resource.__init__(self, "Food", 5, 10)

class Lumber(Resource):
  def __init__(self):
    Resource.__init__(self, "Food", 50, 30)

def initResourceMap():
  Functions.registerResource(Food())
  Functions.registerResource(Lumber())