from turtle import *
import time
import pygame
import tkinter as tk
from tkinter import messagebox

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 means the audio will loop indefinitely

audio_workout_time ="sound1.mp3"
audio_break_time ="sound2.mp3"

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
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer for Workout")
        master.geometry("400x215") # set window size
        self.workout_time_frame = tk.Frame(master)
        self.workout_time_label = tk.Label(self.workout_time_frame, text="Workout Time:")
        self.workout_time_label.pack(side=tk.LEFT)
        self.workout_time_entry = tk.Entry(self.workout_time_frame)
        self.workout_time_entry.pack(side=tk.LEFT)
        self.workout_time_frame.pack(ipadx=15, ipady=15)

        self.break_time_frame = tk.Frame(master)
        self.break_time_label = tk.Label(self.break_time_frame, text="Break Time:")
        self.break_time_label.pack(side=tk.LEFT)
        self.break_time_entry = tk.Entry(self.break_time_frame)
        self.break_time_entry.pack(side=tk.LEFT)
        self.break_time_frame.pack(ipadx=15, ipady=15)

        self.cycles_frame = tk.Frame(master)
        self.cycles_label = tk.Label(self.cycles_frame, text="Cycles:")
        self.cycles_label.pack(side=tk.LEFT)
        self.cycles_entry = tk.Entry(self.cycles_frame)
        self.cycles_entry.pack(side=tk.LEFT)
        self.cycles_frame.pack(ipadx=15, ipady=15)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()
        
    def start(self):
        if not self.workout_time_entry.get().isdigit():
            messagebox.showerror("Error", "Workout time must be a number")
            return
        if not self.break_time_entry.get().isdigit():
            messagebox.showerror("Error", "Break time must be a number")
            return
        if not self.cycles_entry.get().isdigit():
            messagebox.showerror("Error", "Cycles must be a number")
            return
        workout_time = int(self.workout_time_entry.get())
        break_time = int(self.break_time_entry.get())
        cycles = int(self.cycles_entry.get())
        for _ in range(cycles):
            # Record the start time
            start_time = time.perf_counter()
            i = workout_time
            execution_time = 0
            play_audio(audio_workout_time)
            while execution_time < workout_time:
                t.color(colors[i % len(colors)])
                t.clear()
                t.circle(200, (workout_time - i) * 360 / workout_time)
                k.write(i, align='center', font=('Arial', 64, 'bold'))
                update()
                time.sleep(0.9)
                k.clear()  # Clear the text
                i -= 1
                end_time = time.perf_counter()
                execution_time = end_time - start_time
            pygame.mixer.music.stop()
            # Record the end time
            print(f"The execution time is: {execution_time:.6f} seconds")
            
            start_time = time.perf_counter()
            i = break_time
            execution_time = 0
            while execution_time < break_time:
                play_audio(audio_break_time)
                t.color("grey")
                t.clear()
                t.circle(200, (break_time - i) * 360 / break_time)
                k.write(i, align='center', font=('Arial', 64, 'bold'))
                update()
                time.sleep(0.9)
                k.clear()
                i -= 1
                end_time = time.perf_counter()
                execution_time = end_time - start_time
            pygame.mixer.music.stop()
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"The execution time is: {execution_time:.6f} seconds")
        k.write("Done!", align='center', font=('Arial', 64, 'bold'))    
        done()

root = tk.Tk()
gui = GUI(root)
root.mainloop()


