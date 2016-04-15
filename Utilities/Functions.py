'''
 * File: Functions.py
 * Date: 12-02-26
 *
 * Desc: Utility-functions, such as generators
 *
 * Author: H. N. Skjevling
'''

_currentEntityId = -1

def getNewId():
  global _currentEntityId
  _currentEntityId += 1
  return _currentEntityId


ResourceFlyWeightMap = {} #{"Name": ResourceInstance}

def registerResource(resource): #What about uniqueness? Is ID better or needed in addition?
  ResourceFlyWeightMap[resource.getName()] = resource

def registerResources(resources):
  for entries in resources:
    registerResource(entries)

'''
* This should be how all resources are used (programmatically) - Flyweight
* Lookup the resources in e.g a node, then call this function by name to get the usable ResourceInstance
'''
def getResource(name):
  return ResourceFlyWeightMap[name]


ItemFlyWeightMap = {} #{"Name": ItemInstance}

def registerItem(item):
  ItemFlyWeightMap[item.getName()] = item

def registerItems(items):
  for entries in resources:
    registerItem(entries)

'''
* This should be how all items are used (programmatically) - Flyweight
* Lookup the item in e.g an inventory, then call this function by name to get the usable ItemInstance
'''
def getItem(name):
  return ItemFlyWeightMap[name]