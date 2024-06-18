# self represent the current object 
class Person:
  def __init__(self, name):
      self.name = name
  def talk(self):
      print(f'Hi, I am {self.name}')


john = Person('William')
print(john.name)
john.talk()