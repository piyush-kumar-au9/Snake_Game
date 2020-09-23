import random 
import curses
from curses import textpad
import pandas as pd
from datetime import datetime




# Function to create food
def create_food(snake, gamearena):
    food = None
    while food is None:
        # food position
        food  = [random.randint(gamearena[0][0]+1, gamearena[1][0]-1),
                 random.randint(gamearena[0][0]+1, gamearena[1][0]-1)]
        
        # to check whether food and snake coordinates are same
        if food in snake:
            food = None
    return food
        

def main(stdscr):
    
    # inital settings
    curses.curs_set(0) # to make the cursor invisible 
    stdscr.nodelay(1) # to deactivate blocking input
    stdscr.timeout(100)
    

    
    
    
    # to make the game arena
    sh, sw = stdscr.getmaxyx() #to get screen coordinates
    gamearena = [[2,2] ,[sh-2, sw-2]] 
    textpad.rectangle(stdscr, gamearena[0][0], gamearena[0][1], gamearena[1][0], gamearena[1][1])
    
    
    # High score and score display
    global high_score
    high_score_text = "High Score: {}".format(high_score)
    stdscr.addstr(1, sw//2+12, high_score_text)
    
    global score
    score_text = "Score: {}".format(score)
    stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
    
    
    
    
    # to make snake body and setting initial direction
    # coordinates are sw//2+1 ,sw//2, sw//2-1 as my initial direction is right
    # so it will like 321>>(example)
    snake = [[sh//2 , sw//2+1],[sh//2, sw//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addstr(y,x, "#")
    
        
    # Making food available in gamearena
    food = create_food(snake, gamearena)
    stdscr.addstr(food[0], food[1], "O")

    # to make the snake movable
    while True:
        # non-blocking input
        key = stdscr.getch()
        
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key
        
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
            
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]
            
            
        stdscr.addstr(new_head[0], new_head[1], "#")
        snake.insert(0, new_head)
        
        
        # Snake moving and eating the food and increasing the size
        if snake[0] == food:
            score+=1
            score_text = "Score: {}".format(score)
            stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
            
            
            
            
            food = create_food(snake, gamearena)
            stdscr.addstr(food[0], food[1], "O")
        else: 
            stdscr.addstr(snake[-1][0], snake[-1][1], " ")
            snake.pop()
        
        
        # to make the condition when game is over
        if (snake[0] in snake[1:] or
            snake[0][0] in [gamearena[0][0], gamearena[1][0]] or
            snake[0][1] in [gamearena[0][1], gamearena[1][1]]):
            message = "!!!!Game Over!!!!"
            stdscr.addstr(sh//2, sw//2 - (len(message)//2), message)
            
            stdscr.nodelay(0) #to activate blocking input
            stdscr.getch()
            break
        stdscr.refresh()



if  __name__ == "__main__":
    
    score_data = pd.read_csv("Scorecard.csv")
    high_score = score_data["Score"].max() 
    score = 0
    
    curses.wrapper(main)
    
    
    # Storing the score with present datetime
    if score >= high_score:
        score_data = score_data.append({"Datetime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        "Score": score}, ignore_index = True)
        score_data.to_csv("Scorecard.csv", index = None)
