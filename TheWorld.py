'''
 * File: TheWorld.py
 * Date: 12-02-27
 *
 * Desc: An "Engine". Contains everything, and updates everything.
 *
 * Author: H. N. Skjevling
'''

import Utilities.Functions
import traceback

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class BaseEntity:
  def __init__(self, name):
    self._name = name
    self._id = Utilities.Functions.getNewId()
    self._position = Position(0.0, 0.0)
    print self.getName()

  def getName(self):
    return self._name

  def getId(self):
    return self._id

  def getPosition(self):
    return self._position

class MainMan:
  def __init__(self, entities):
    self._entities = entities

  def addEntity(entity):
    if(self._entities.count(entity) < 1):
      self._entities.append(entity)

  def removeEntity(entity):
    if(self._entities.count(entity) > 0):
      self._entities.remove(entity)

  def populateFromFile(filename):
    try:
      file = open(filename, 'r')
      for line in file:
          position = []
          splitLine = line.strip().split(',')
          if splitLine.count() != 3:
            error("populateFromFile", "Invalid number of arguments in line")
          entityType, coord_x, coord_y = 
          if(entityType)
    except Exception, ex:
      print ex



  def update(self, elapsed):
    try:
      for entity in self._entities:
        entity.update(elapsed)
    except Exception, ex:
      raise