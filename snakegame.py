import random
import os
WIDTH = 20
HEIGHT = 10
# Snake stored in simple array
snake = [[5,5], [4,5], [3,5]]
direction = "RIGHT"
food = [random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)]
score = 0
def draw():
    os.system("cls" if os.name=="nt" else "clear")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x,y] == snake[0]:
                print("O", end="")
            elif [x,y] in snake:
                print("o", end="")
            elif [x,y] == food:
                print("X", end="")
            elif x==0 or x==WIDTH-1 or y==0 or y==HEIGHT-1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print("Score:", score)
while True:
    draw()
    print("W=Up S=Down A=Left D=Right")
    move = input("Move: ").upper()
    if move=="W": direction="UP"
    elif move=="S": direction="DOWN"
    elif move=="A": direction="LEFT"
    elif move=="D": direction="RIGHT"
    head = snake[0].copy()
    if direction=="UP": head[1]-=1
    elif direction=="DOWN": head[1]+=1
    elif direction=="LEFT": head[0]-=1
    elif direction=="RIGHT": head[0]+=1
    # Collision
    if head in snake or head[0]==0 or head[0]==WIDTH-1 or head[1]==0 or head[1]==HEIGHT-1:
        print("Game Over")
        print("Final Score:",score)
        break
    # Add new head
    snake.insert(0, head)
    # Eat food
    if head == food:
        score += 1
        food = [random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)]
    else:
        snake.pop()   # remove tail