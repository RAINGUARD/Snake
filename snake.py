import curses
from random import randint

#set up window
curses.initscr()
win = curses.newwin(20, 60, 0, 0) # new window with 20 rows, 60 columns
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# establish variables
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)
score = 0
speed = 180
ESC = 27
key = curses.KEY_RIGHT # set first input manually so that the snake starts in motion

win.addch(food[0], food[1], '#') # add first food to window

# While loop runs the game until user presses
# escape key, or loses the game
while key != ESC:
    win.addstr(0,2, 'Score ' + str(score) + ' ') # add score to display
    win.addstr(0, 41, 'Press ESC to Exit')       # add instructions to display
    
    win.timeout(speed - (len(snake)) // 5 + len(snake)//10 % 120) # control snake speed

    # register new input
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    # make sure the input is valid
    if key == curses.KEY_RIGHT and prev_key == curses.KEY_LEFT:
        key = prev_key
    if key == curses.KEY_LEFT and prev_key == curses.KEY_RIGHT:
        key = prev_key
    if key == curses.KEY_UP and prev_key == curses.KEY_DOWN:
        key = prev_key
    if key == curses.KEY_DOWN and prev_key == curses.KEY_UP:
        key = prev_key
    if key not in[curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    # check if we hit the wall
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # check if snake hits itself
    if snake[0] in snake[1:]: break

    #check if hit food
    if snake[0] == food:
        score += 1
        if speed >40: # increase snake speed after getting food
            speed -= 10
        food = ()
        while food == (): # place new food in random location
            food = (randint(1,18), randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # making the snake move
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')
   

curses.endwin()
print(f"Final score = {score}") # print final score