import turtle
import time
import random

# create window - done
# get number of racers - done
# create the turtles
# race the turtles



# define window size
WIDTH, HEIGHT = 500, 400
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'pink', 'purple', 'brown', 'cyan']

def getNumberOfRacers():
 racers = 0
 valid = False
 while not valid:
   racers = input("How many racers would you like? choose range 2-10: ")
   if int(racers) not in [2, 3, 4, 5, 6, 7, 8, 9]:
     print("invalid input") 
   else:
     racers = int(racers)
     valid = True
     return racers

def initTurtle():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title('Kentucky Derby')

def createTurtles(colors):
  spacingx = WIDTH // (len(colors)+1)
  turtles = []
  for i, color in enumerate(colors):
    racer = turtle.Turtle()
    racer.shape('turtle')
    racer.color(color)
    racer.left(90)
    racer.penup()

    racer.setpos(-WIDTH//2 + (i+1)* spacingx, -HEIGHT//2 + 20)

    racer.pendown()
    turtles.append(racer)
  return turtles

def race(colors):
  turtles = createTurtles(colors)
  while True:
    for racer in turtles:
      distance = random.randrange(1, 20)
      racer.forward(distance)

      x,y = racer.pos()
      if y >= HEIGHT //2 -10:
        return colors[turtles.index(racer)]



racers = getNumberOfRacers()
initTurtle()


random.shuffle(COLORS)
colors = COLORS[:racers]
print("The winner is: " + race(colors))

time.sleep(5)


