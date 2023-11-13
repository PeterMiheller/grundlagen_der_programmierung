import turtle
import time
t=turtle.Pen()
def A():
    t.pensize(5)
    t.left(110)
    t.forward(50)
    t.left(140)
    t.forward(50)
    t.backward(15)
    t.left(110)
    t.forward(25)
    print(t.position())
    t.up()
    t.home()
    t.down()


def B():
    t.pensize(4)
    t.left(90)
    t.forward(40)
    t.circle(-15,200)
    t.forward(20)
    t.left(180)
    t.circle(-15,250)
    t.forward(30)
    print(t.position())
    t.up()
    t.home()
    t.down()


def C():
    t.pensize(5)
    t.circle(25,-180)
    print(t.position())
    t.up()
    t.home()
    t.down()


def D():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.right(150)
    t.forward(50)
    t.right(110)
    t.forward(25)
    print(t.position())
    t.up()
    t.home()
    t.down()

def E():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.down()
    t.forward(20)

def F():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.down()

def G():
    t.pensize(5)
    t.circle(25, -180)
    t.up()
    t.circle(25,180)
    t.down()
    t.circle(15,100)
    t.left(80)
    t.forward(20)
    t.up()
    t.backward(20)
    t.right(80)
    t.circle(15, -100)
    t.down()
    t.up()
    t.home()
    t.down()

def H():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.backward(22)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(22)
    t.backward(45)
    t.right(90)

def I():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(10)
    t.backward(20)
    t.up()
    t.forward(10)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.down()
    t.backward(10)
    t.forward(20)

def J():
    t.pensize(5)
    t.circle(15,-90)
    t.up()
    t.circle(15,90)
    t.down()
    t.left(90)
    t.forward(45)
    t.backward(45)
    t.right(90)

def K():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.backward(25)
    t.right(45)
    t.forward(25)
    t.backward(25)
    t.left(45)
    t.right(180)
    t.left(45)
    t.forward(25)
    t.left(45)

def L():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.backward(45)
    t.right(90)
    t.forward(25)

def M():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.right(135)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(135)
    t.forward(45)
    t.left(90)

def N():
    t.pensize(5)
    t.left(90)
    t.forward(45)
    t.right(155)
    t.forward(50)
    t.left(155)
    t.forward(45)
    t.backward(45)
    t.right(90)


def menu():
    return""""
    Turtle Paint v1.0

    1. Textnachricht zeichnen
    2. Neues Zeichen hinzufügen
    0. Exit

    """
def main():
    distance_between_letters = 0
    while True:
        print(menu())
        try:
            opt=int(input('Was möchten Sie zeichnen?\n '))
            if opt==1:
                x=-325.00+distance_between_letters
                y=250.00
                n=1
                while n>0:
                    t.teleport(x,y)
                    lit=input('Wählen Sie Litter:\n ')
                    if lit== 'A':
                        A()
                    if lit == 'B':
                        B()
                    if lit== 'C':
                        C()
                    if lit== 'D':
                        D()
                    if lit== 'E':
                        E()
                    if lit == 'F':
                         F()
                    if lit == 'G':
                        G()
                    if lit == 'H':
                        H()
                    if lit == 'I':
                        I()
                    if lit == 'J':
                        J()
                    if lit == 'K':
                        K()
                    if lit == 'L':
                        L()
                    if lit == 'M':
                        M()
                    if lit == 'N':
                        N()
                    n-=1

            if opt==2:
                pass
            if opt==0:
                break
        except ValueError:
            print('')
            print('Bitte ein Zahl zwischen 0 und 2 eingeben')


main()
turtle.done()

