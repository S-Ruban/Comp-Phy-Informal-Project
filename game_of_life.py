import pygame   # used pygame to draw and colour the board


def step():     # this function updates the state of the board
    for i in range(rows):
        for j in range(cols):
            # counting number of alive neighbours for each cell
            c = board[i-1][(j-1) % cols]+board[(i-1) % rows][j]+board[(i-1) % rows][(j+1) % cols]+board[i][(j-1) % cols] + \
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


# RGB values of colours used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105, 105, 105)

# width and height of each cell
WIDTH = 20
HEIGHT = 20

MARGIN = 2      # margin between each cell

board = []      # the original board
board2 = []     # temporary copy of original board
rows, cols = (10, 10)   # defining dimensions of board
for i in range(rows):
    board.append([])
    board2.append([])
    for j in range(cols):
        board[i].append(0)
        board2[i].append(0)

# define initial conditions here
board[2][1] = 1
board[2][2] = 1
board[2][3] = 1
board[1][3] = 1
board[0][2] = 1


pygame.init()
screen = pygame.display.set_mode([(WIDTH+MARGIN)*rows, (WIDTH+MARGIN)*cols])
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
screen.fill(GREY)

done = False

# loop until the user clicks the close button.
while not done:
    step()
    copy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for i in range(rows):
        for j in range(cols):
            color = WHITE
            if board[i][j] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(1)   # rate of change of state
    pygame.display.flip()

pygame.quit()
