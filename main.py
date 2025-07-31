import tkinter as tk
import random
import os

# Voice function using PowerShell
def speak(text):
    os.system(f"powershell -Command \"Add-Type –AssemblyName System.Speech; " +
              f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}');\"")

# Game setup
computer = random.randint(1, 100)
guesses = 0

# Function to check guess
def check():
    global guesses
    try:
        a = int(entry.get())
        if a > computer:
            guesses += 1
            result_label.config(text="Enter a lower number")
            speak("Enter a lower number")
        elif a < computer:
            guesses += 1
            result_label.config(text="Enter a higher number")
            speak("Enter a higher number")
        else:
            result_label.config(
                text=f"🎉 Correct! You guessed in {guesses} attempts.\nComputer chose {computer}"
            )
            speak("Congratulations! You guessed the correct number.")
            speak(f"You took {guesses} attempts.")
    except:
        result_label.config(text="Please enter a valid number")
        speak("Please enter a valid number")

# GUI window
root = tk.Tk()
root.title("Alok's Number Guessing Game")
root.geometry("400x300")

# Welcome voice
speak("Welcome to Alok Gaming world. Welcome to the number guessing game")

# Heading
heading = tk.Label(root, text="Number Guessing Game", font=("Arial", 16))
heading.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button
check_btn = tk.Button(root, text="Guess", font=("Arial", 12), command=check)
check_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

