import pygame   # used pygame to draw and colour the board
import random
import matplotlib.pyplot as plt


def step():     # this function updates the state of the board
    for i in range(rows):
        for j in range(cols):
            # counting number of alive neighbours for each cell
            c = board[(i-1) % rows][(j-1) % cols]+board[(i-1) % rows][j]+board[(i-1) % rows][(j+1) % cols]+board[i][(j-1) % cols] + \
                board[i][(j+1) % cols]+board[(i+1) % rows][(j-1) % cols] + \
                board[(i+1) % rows][j]+board[(i+1) % rows][(j+1) % cols]
            if(board[i][j] == 1):       # if that cell is alive
                if(c < 2 or c > 3):     # underpopulation/overpopulation
                    board2[i][j] = 0
                else:
                    board2[i][j] = 1
            else:
                if(c == 3):             # perfect conditions for a dead cell to come to life
                    board2[i][j] = 1
                else:
                    board2[i][j] = 0


def copy():     # transfer contents of duplicate board to original board
    for i in range(rows):
        for j in range(cols):
            board[i][j] = board2[i][j]


def count():
    c = 0
    for i in range(rows):
        for j in range(cols):
            c += board[i][j]
    return(c)


# RGB values of colours used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# width and height of each cell
WIDTH = 5
HEIGHT = 5

MARGIN = 2      # margin between each cell

p = 0.5    # probability p
T = 0       # T is the number of iterations
s = 0

iters = []
pop = []

board = []      # the original board
board2 = []     # temporary copy of original board
rows, cols = (150, 100)   # defining dimensions of board
for i in range(rows):
    board.append([])
    board2.append([])
    for j in range(cols):
        board[i].append(0)
        board2[i].append(0)

# define initial conditions here
for i in range(rows):
    for j in range(cols):
        RAND = random.random()
        if(RAND < p):
            board[i][j] = 1
        else:
            board[i][j] = 0


pygame.init()
screen = pygame.display.set_mode([(WIDTH+MARGIN)*rows, (WIDTH+MARGIN)*cols])
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
screen.fill(BLACK)

done = False

iters.append(T)
pop.append(count())

# loop until the user clicks the close button.
while not done:
    temp = count()
    step()
    copy()
    T += 1
    # if(isPowerOfTwo(T)):
    #     print(T, " ", count())
    if temp == count():
        s += 1
    # if s == 10:
    #     done = True
    iters.append(T)
    pop.append(count())
    if count() == 0:
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for i in range(rows):
        for j in range(cols):
            color = BLACK
            if board[i][j] == 1:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * i + MARGIN,
                              (MARGIN + HEIGHT) * j + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(50)   # rate of change of state
    pygame.display.flip()

pygame.quit()

# print(iters)
# print(pop)
plt.plot(iters, pop)
plt.show()
