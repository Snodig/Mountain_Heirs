'''
 * File: Worldgen.py
 * Date: 12-02-27
 *
 * Desc: An "Engine". Contains everything, and updates everything.
 *
 * Author: H. N. Skjevling
'''

import random
random.seed()

class Topology:
  def __init__(self, width, height):
    self._coordinates = [[0]]
    self._width = width
    self._height = height

  def getWidth(self):
    return self._width

  #Note to self: Fuck height
  def getHeight(self):
    return self._height

  def generateHeightMap(self):
    i = 0
    maxi = 100
    num = 0
    while i < maxi:
      num = random.randint(num-1, num+1)
      print num * "."

'''

    for i in range(0, self.getWidth()):
      horizontals = []
      if i == 0:
        horizontals.append(0)
      else:
        horizontals.append(self._coordinates[i-1][0])
      for j in range(0, self.getHeight()):
        if j == 0:
          horizontals.append(randomHeight(horizontals[j]))
        else:
          horizontals.append(randomHeight(horizontals[j-1]))
      self._coordinates.append(horizontals)

      '''

def randomHeight(relativePoint):
  result = random.randint(relativePoint-1, relativePoint+1)

  print int(result) * "."
  return result