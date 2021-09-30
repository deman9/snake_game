from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Garr snake game')
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

# collision with food detection
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend_snake()

# collision with wall detection
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

# collision with head detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
