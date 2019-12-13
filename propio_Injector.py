import os
from pprint import pprint

class Factory:
   def __init__(self, allowReplace=False):
      self.providers = {}
      self.allowReplace = allowReplace
   def Provide(self, feature, provider, *args, **kwargs):
      if not self.allowReplace:
         assert not feature in self.providers.keys(), "Duplicate feature: %r" % feature
      if callable(provider):
         def call(): return provider(*args, **kwargs)
      else:
         def call(): return provider
      self.providers[feature] = call
      #print(f"feature: {feature}  type_of_feature: {type(feature)}  call:{call}")
   def __getitem__(self, feature):
      #print(f"Factory getitem was called")
      try:
         provider = self.providers[feature]
      except KeyError:
         raise KeyError("Unknown feature named %r" % feature)
      return provider()

features = Factory()

#
# Some basic assertions to test the suitability of injected features
#

def NoAssertion(obj): return True   # assertion by default

def IsInstanceOf(*classes):    # return a function that checks if an object is an instance of a class
   def test(obj): return isinstance(obj, classes)
   return test

def HasAttributes(*attributes):  # return if the attributes belong to an especific object
   def test(obj):
      for each in attributes:
         if not hasattr(obj, each): return False
      return True
   return test

def HasMethods(*methods):
   def test(obj):
      for each in methods:
         try:
            attr = getattr(obj, each)
         except AttributeError:
            return False
         if not callable(attr): return False
      return True
   return test



class RequiredFeature(object):
   def __init__(self, feature, assertion=NoAssertion):
      self.feature = feature
      self.assertion = assertion
   def __get__(self, obj, T):
      return self.result # <-- will request the feature upon first call
   def __getattr__(self, name):
      #print(f'getattr --> object: {self}   name: {name}')
      assert name == 'result', "Unexpected attribute request other then 'result'"
      self.result = self.Request()
      #print(f"self.result es {self.result}")
      return self.result
   def Request(self):
      obj = features[self.feature]
      assert self.assertion(obj), \
             "The value %r of %r does not match the specified criteria" \
             % (obj, self.feature)
      return obj
"""
class Component(object):
   "Symbolic base class for components"
"""
#### DEMO

class Bar():
   console   = RequiredFeature('Console', HasMethods('WriteLine'))
   title = RequiredFeature('AppTitle', IsInstanceOf(str))
   user  = RequiredFeature('CurrentUser', IsInstanceOf(str))
   def __init__(self):
      self.proof_var = 0
   def PrintYourself(self):
      self.console.WriteLine('-- Bar instance --')
      self.console.WriteLine('Title: %s' % self.title)
      self.console.WriteLine('User: %s' % self.user)
      self.console.WriteLine('proof_var: %d' % self.proof_var)



class SimpleConsole():
   def WriteLine(self, s):
      print(s)



class BetterConsole():
   def __init__(self, prefix=''):
      self.prefix = prefix
   def WriteLine(self, s):
      lines = s.split('\n')
      for line in lines:
         if line:
            print(self.prefix, line)
         else:
            print()



def GetCurrentUser():
   return os.getenv('USERNAME') or 'UNI' # USERNAME is platform-specific


if __name__ == '__main__':
   print('\n*** Demo ***')
   features.Provide('AppTitle', 'My own container ...\n\n... by my team')
   features.Provide('CurrentUser', GetCurrentUser)
   features.Provide('Console', BetterConsole, prefix='#####') # <-- transient lifestyle
   
   bar = Bar()
   bar.PrintYourself()

