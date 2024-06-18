class Point:
  # Method that print "move" in terminal
  def move(self):
    print('move')
    
 # Method that print "draw" in terminal
  def draw(self):
    print('draw')

# instance of ours class Point
point1 = Point()
# added attributes in object
point1.x = 30
point1.y = 10
# print attributes point.x
print(point1.x)

# print method of ours class Point
point1.draw()
point1.move()

point2 = Point()
point2.x = 40

print(point2.x)