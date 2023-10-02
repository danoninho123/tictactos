"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
    eu dei a cor red para o X e blue para o circulo
    codigo cor     
    color('red')
    color('blue')
    codigo tamanho x
    line(x+30, y+30, x + 90, y + 90)
    line(x+30, y + 90, x + 90, y+30)
    codigo tamanho o
    circle(35)
2. What happens when someone taps a taken spot?
    aparece x ou o
3. How would you detect when someone has won?
    eu faria uma lista com variaves tipo isso 
    ==>   wins = [  [0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
    colocaria if para chegar se alguns dessas variaves foi feita. colocando o codigo de verificação para roda assim 
    que o ultimo quadrado fosse marcado

4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    line(x+30, y+30, x + 90, y + 90)
    line(x+30, y + 90, x + 90, y+30)
    


def drawo(x, y):
    """Draw O player."""
    color('red')
    up()
    goto(x + 67, y + 30)
    down()
    circle(35)
    color('red')


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx,drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
