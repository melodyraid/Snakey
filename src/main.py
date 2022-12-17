"imports tkinter stuff and rnjesus"
from tkinter import Tk, Label, Canvas, ALL
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 90
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#8263fd" # Purple
FOOD_COLOR = "#FF0000" # Red
BACKGROUND_COLOR = "#000000" # Black


class Snake:
    "Spawns arab sanek"
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        # maybe change starting coordinates
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                tag="snake",
                )
            self.squares.append(square)

class Food:
    "Taberu!"
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-2) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-2) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="apple")


def next_turn(snake, apple):
    "Don't kill yourself"
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == apple.coordinates[0] and y == apple.coordinates[1]:
        global score
        score += 1
        label.config(text="Score {}".format(score))
        canvas.delete("apple")
        apple = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(
            SPEED,
            next_turn,
            snake,
            apple,
            )

def change_direction(new_direction):
    "Do not seppuku"

    global direction

    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

def check_collision(sanek):
    "checks collision"

    x, y = sanek.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in sanek.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    "Why yu seppuku :("

    canvas.delete(ALL)
    canvas.create_text(
        (canvas.winfo_width() / 2),
        (canvas.winfo_height() / 2),
        font=('consolas', 70),
        text=" Baka Mitai\nバカ みたい",
        fill="red",
        tag="gameover")

window = Tk()
window.title("Snakey")

score = 0
direction = 'down'

label = Label(
    window,
    text=f"Score: {score}",
    font=('consolas', 40),
    )
label.pack()

canvas = Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=GAME_HEIGHT,
    width=GAME_WIDTH,
    )
canvas.pack()

window.update()

window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height))

window.geometry(f"{window_height}x{window_width}+{x}+{y}")

window.bind(('w'), lambda event: change_direction('up'))
window.bind(('a'), lambda event: change_direction('left'))
window.bind(('s'), lambda event: change_direction('down'))
window.bind(('d'), lambda event: change_direction('right'))


snake = Snake()
apple = Food()

next_turn(snake, apple)

window.mainloop()

# I wanna drink another monster
