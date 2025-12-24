import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly create a car
    import random
    if random.randint(1, 6) == 1:
        car_manager.create_car()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    car_manager.move_cars()
    if player.is_at_the_finish_line():
        player.starting_position()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
