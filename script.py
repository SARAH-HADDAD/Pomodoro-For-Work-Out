from turtle import *
import time
from playsound import playsound
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer for Workout")
        master.geometry("400x180") # set window size
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

        #self.start_button = tk.Button(master, text="Start", command=self.start)
        #self.start_button.pack()

root = tk.Tk()
gui = GUI(root)
root.mainloop()


