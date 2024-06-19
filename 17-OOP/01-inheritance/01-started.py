class Mammal:
  def walk(self):
    print('Walk')

class Dog(Mammal):
  def bark(self):
    print('bark')
  
  # The code defines a class `Cat` that inherits from `Mammal`, with methods `Meow` and `walk` being
  # called on an instance of `Cat`.
  
class Cat(Mammal):
  def Meow(self):
    print('Meow')


cat1 = Cat()
cat1.Meow(
)

cat1.walk()