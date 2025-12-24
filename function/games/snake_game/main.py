from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def next_program():
    print("🚀 Next program started")
    # এখানে next game / menu চালাও
    # example:
    # import menu
    # menu.start()


def game_on():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    is_game_on = True

    # ✅ ONLY stop the loop (DO NOT destroy screen here)
    def on_close():
        nonlocal is_game_on
        is_game_on = False

    screen.getcanvas().winfo_toplevel().protocol(
        "WM_DELETE_WINDOW", on_close
    )

    # 🎮 GAME LOOP
    while is_game_on:
        try:
            screen.update()
            time.sleep(0.1)
            snake.move_snake()
        except:
            # safety net (extra protection)
            break

        # Food collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Wall collision
        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            scoreboard.reset()
            snake.reset_snake()

        # Tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset_snake()

    # ✅ NOW it is safe
    try:
        screen.bye()
    except:
        pass

    next_program()


game_on()
