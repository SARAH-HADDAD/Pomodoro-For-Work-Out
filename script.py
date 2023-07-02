import time
from playsound import playsound

def workout_timer(total_time, workout_time, rest_time):
    cycles = total_time // (workout_time + rest_time)

    for _ in range(cycles):
        print("Entraînement de {} secondes".format(workout_time))
        time.sleep(workout_time)
        play_sound("breath.mp3")
        print("Repos de {} secondes".format(rest_time))
        time.sleep(rest_time)
        play_sound("breath.mp3")

    print("Entraînement terminé !")

def play_sound(sound_file):
    playsound(sound_file)

# Paramètres de la minuterie Pomodoro pour l'entraînement (en secondes)
total_time = 600  # Temps total d'entraînement en secondes (10 minutes)
workout_time = 30  # Durée de l'entraînement en secondes
rest_time = 10  # Durée du repos en secondes

workout_timer(total_time, workout_time, rest_time)
