'''
 * File: Actors.py
 * Date: 12-02-27
 *
 * Desc: All actors and mobiles
 *
 * Author: H. N. Skjevling
'''

from TheWorld import Position, BaseEntity
from Utilities import Functions
from Entities import Items, Resources

class Physique:
  def __init__(self, walkingSpeed, runningSpeed):
    self.walkingSpeed = walkingSpeed
    self.runningSpeed = runningSpeed
    self.fatigue = 0.0
    self.health = 1.0 # 1 == healthy, <= 0.5 == sick, 0 == incapacitated
    self.hunger = 0.0 # <= 0.2 == full, >= 0.5 == hungry,  >=0.8 == starving, 1 == dead

class Mobile:
  def __init__(self, physique, position):
    self._physique = physique
    self._position = position
    self._inventory = { "Items": {}, "Resources": {} }
    self._timers = { "Hunger": 0.0 }

  def addItem(self, name, amount=1):
    if(amount < 1):
      return
    else:
      self._inventory["Items"][name] += amount

  def removeItem(self, name, amount=1):
    if(amount < 1):
      return
    else:
      self._inventory["Items"][name] -= amount

  def countItem(self, name):
    return self._inventory["Items"].count(name)

  def addResource(self, name, amount=1):
    if(amount < 1):
      return
    else:
      self._inventory["Resources"][name] += amount

  def removeResource(self, name, amount=1):
    if(amount < 1):
      return
    else:
      self._inventory["Resources"][name] -= amount

  def countResource(self, name):
    return self._inventory["Resources"].count(name)

  def getPhysique(self):
    return self._physique

  def getPosition(self):
    return self._position

class Person(BaseEntity, Mobile): 
  def __init__(self, name):
    BaseEntity.__init__(self, name)
    Mobile.__init__(self, Physique(1, 3), Position(0, 0))
    self._elapsed = 0.0

  def update(self, elapsed):
    self._elapsed += elapsed
    if(self._elapsed >= 2.0):
      print self.getName(), " was updated. (Did nothing)"
      self._elapsed = 0.0

class Animal(BaseEntity, Mobile):
  def __init__(self, physique, position):
    BaseEntity.__init__(self, self.__class__.__name__)
    Mobile.__init__(self, physique, position)

  def update(self, elapsed):
    self._timers["Hunger"] += elapsed

    if(self._timers["Hunger"] >= 20.0):
      self._timers["Hunger"] = 0.0
      self.getPhysique().hunger += 0.1
      hunger = self.getPhysique().hunger

      if(hunger == 1.0):
        print self.getName(), "has died from starvation: x.x"

      elif(hunger >= 0.8):
        print self.getName(), "is starving: ._."

      elif(hunger >= 0.5):
        print self.getName(), "is hungry: >_<"

class Bear(Animal):
  def __init__(self):
    Animal.__init__(self, Physique(0.5, 5.0), Position(0, 0))

  def update(self, elapsed):
    Animal.update(self, elapsed)