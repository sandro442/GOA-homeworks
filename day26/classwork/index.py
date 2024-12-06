# 1) შევქმნათ ფუნქცია turtle ში დაარქვით walk() იგი წავა 200-ით fall_back() დაატრიალებს და წამოვა უკან ჩვენი დანიშნულებაა, რომ ამ როი ფუქნციის გარდ ადაიწეროს ეს ინფორმაცია 1 ფუქნციის გამოყენებით go_and_back()

from turtle import *

def walk():
    forward(200)
def walk_back():
    left(180)
    forward(200)
def go_and_back():
    walk()
    walk_back()

exitonclick()