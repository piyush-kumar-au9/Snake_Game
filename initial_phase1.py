# -*- coding: utf-8 -*-
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

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)