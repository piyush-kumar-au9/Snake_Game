import random 
import curses
from curses import textpad

def main(stdscr):
    
    # inital settings
    curses.curs_set(0) # to make the cursor invisible 
    
    # to make the game arena
    sh, sw = stdscr.getmaxyx() #to get screen coordinates
    gamearena = [[2,2] ,[sh-2, sw-2]] 
    textpad.rectangle(stdscr, gamearena[0][0], gamearena[0][1], gamearena[1][0], gamearena[1][1])
    
    # to make snake body and setting initial direction
    # coordinates are sw//2+1 ,sw//2, sw//2-1 as my initial direction is right
    # so it will like 3,2,1(example)
    snake = [[sh//2 , sw//2+1],[sh//2, sw//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addstr(y,x, ">")
    
    
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

