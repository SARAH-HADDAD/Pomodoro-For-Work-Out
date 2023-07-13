from turtle import *
import time
from playsound import playsound

def play_sound(sound_file):
    playsound(sound_file)

bgcolor("black")
t = Turtle()

t.speed(0)
t.shape("circle")
t.shapesize(0.3)
t.width(5)
t.pu()
t.goto(0, -200)
t.pd()

delay(0)
speed(0)
ht()
colors = ["red","tomato","salmon", "orange","gold", "yellow","lime","wheat","olive","green","teal","cyan","coral","aquamarine","skyblue", "blue","indigo","violet", "purple", "white","plum", "pink","orchid"]

countdown = 20
i= countdown
while i >= 0:
    t.color(colors[i % len(colors)])
    t.clear()
    t.circle(200, (countdown-i) * 360/countdown)
    color('white')
    write(countdown, align='center', font=('Arial', 48, 'bold'))
    update()
    time.sleep(1)
    i -= 1
play_sound("breath.mp3")    
done()
