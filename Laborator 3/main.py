import turtle
t = turtle.Pen()
def dreptunghiuri():
    t.speed(2)
    t.color("blue")
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.up()
    t.left(90)
    t.forward(35)
    t.down()
    t.color("red")
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.speed(1)
    t.up()
    t.home()
    t.down()
    t.reset()


def inima():

    t.speed(3)
    t.pensize(5)
    t.color("black","red")
    t.begin_fill()
    t.left(55)
    t.forward(150)
    t.circle(50,200)
    t.right(150)
    t.circle(50,200)
    t.forward(155)
    t.end_fill()
    t.speed(1)
    t.left(180)
    t.reset()


def case():
    t.speed(4)
    t.up()
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.down()
    t.color("black","orange")
    t.begin_fill()
    t.left(90)
    print(t.position())
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.end_fill()
    #usa
    t.color("black","brown")
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.left(90)
    t.backward(30)
    t.up()
    t.forward(30)
    t.down()
    t.forward(90)
    t.up()
    #geamuri
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(20)
    t.down()
    t.color("black","blue")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.up()
    t.left(90)
    t.forward(110)
    t.down()
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.end_fill()
    #acoperis
    t.up()
    t.forward(50)
    t.right(90)
    t.forward(130)
    t.down()
    t.color("black", "red")
    t.begin_fill()
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(200)
    t.end_fill()
    #casa2
    t.teleport(-100.00,-200.00)
    t.color("black","pink")
    t.begin_fill()
    t.right(150)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.end_fill()
    # usa
    t.color("black", "brown")
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.left(90)
    t.backward(30)
    t.up()
    t.forward(30)
    t.down()
    t.forward(90)
    t.up()
    # geamuri
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(20)
    t.down()
    t.color("black", "blue")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.up()
    t.left(90)
    t.forward(110)
    t.down()
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.end_fill()
    # acoperis
    t.up()
    t.forward(50)
    t.right(90)
    t.forward(130)
    t.down()
    t.color("black","red")
    t.begin_fill()
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(200)
    t.end_fill()
    t.speed(1)
    t.up()
    t.home()
    t.down()
    t.reset()

def menu():
    return """
            1- Rechtecke
            2- Herz
            3- Häusern
            0-exit
    """


while True:
    print(menu())
    try:
        opt = int(input('Was haben Sie gewählt? '))
        print('')
        if opt==0:
            break
        if opt == 1:
            dreptunghiuri()

        if opt == 2:
            inima()

        if opt == 3:
            case()

        if opt > 3:
            print('Bitte ein Zahl zwischen 0 und 3 eingeben')

        if opt < 0:
            print('Bitte ein Zahl zwischen 0 und 3 eingeben')

    except ValueError:
        print('')
        print('Bitte ein Zahl zwischen 0 und 3 eingeben')

turtle.done()






