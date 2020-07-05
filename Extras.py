from microbit import *
import random

# Setup initial variables
player_x = 0
player_y = 1
goal_x = 4
goal_y = 4

def update(px,py,gx,gy):
    if(button_a.was_pressed()):
        px = (px + 1) % 5
    if(button_b.was_pressed()):
        py = (py + 1) % 5
    if py < 0:
        py = 4
    if px < 0:
        px = 4
    return px, py, gx, gy

def draw_state(player_x, player_y, goal_x, goal_y):
    r = ""
    for i in range(0,4):
        for j in range(0,4):
            if (i == player_x and j == player_y) or (i == goal_x and j == goal_y):
                r = r + "9"
            else:
                r = r + "0"
        r += ":"
    display.show(Image(r))


#Game loop
while True:
    #Update Movement
    player_x, player_y, goal_x, goal_y = update(player_x, player_y, goal_x, goal_y)
    
    #Check for win
    if(player_x == goal_x and player_y == goal_y):
        display.scroll("Winner")
        goal_x = random.randint(0,5)
        goal_y = random.randint(0,5)
        player_x = random.randint(0,5)
        player_y = random.randint(0,5)
        
    #Draw the current state
    draw_state(player_x, player_y, goal_x, goal_y)
