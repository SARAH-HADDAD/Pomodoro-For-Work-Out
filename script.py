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
k = Turtle()
k.penup()
k.goto(0, 0)  # Position to display the text
k.pendown()
k.color("white")
delay(0)
speed(0)
ht()
colors = ["red","tomato","salmon", "orange","gold", "yellow","lime","wheat","olive","green","teal","cyan","coral","aquamarine","skyblue", "blue","indigo","violet", "purple", "white","plum", "pink","orchid"]

# Paramètres de la minuterie Pomodoro pour l'entraînement (en secondes)
total_time = 600  # Temps total d'entraînement en secondes (10 minutes)
workout_time = 30  # Durée de l'entraînement en secondes
rest_time = 10  # Durée du repos en secondes
cycles = total_time // (workout_time + rest_time)
for _ in range(cycles):
    i = workout_time
    while i >= 0:
        t.color(colors[i % len(colors)])
        t.clear()
        t.circle(200, (workout_time - i) * 360 / workout_time)
        k.write(i, align='center', font=('Arial', 56, 'bold'))
        update()
        time.sleep(1)
        k.clear()  # Clear the text
        i -= 1
    i = rest_time
    while i >= 0:
        t.color("grey")
        t.clear()
        t.circle(200, (rest_time - i) * 360 / rest_time)
        k.write(i, align='center', font=('Arial', 56, 'bold'))
        update()
        time.sleep(1)
        k.clear()
        i -= 1
done()