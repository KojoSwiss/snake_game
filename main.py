from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

start_position = [(0, 0), (-20, 0), (-40, 0)]

for i in start_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(i)







screen.title("Snake 1.0")
screen.exitonclick()