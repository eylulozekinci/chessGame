import tkinter as tk
from tkinter import messagebox

import pygame

# Initialize the mixer for background music
if not pygame.mixer.get_init():
    pygame.mixer.init()
pygame.mixer.music.load("C:\\Program Files\\pygameChess-main\\pygameChess-main\\assets\\media\\Barbie - The Nutcracker (Theme) [Audio]  Barbie in The Nutcracker.mp3")  # Path to your music file
pygame.mixer.music.set_volume(0.5)  # Default volume (50%)

# Function to start two-player mode
def start_two_player_game():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Program Files\\pygameChess-main\pygameChess-main\\assets\\media\\Barbie - The Nutcracker (Theme) [Audio]  Barbie in The Nutcracker.mp3")  # Path to your music file

    pygame.mixer.music.play(-1)  # Start music
    messagebox.showinfo("Two Player Mode", "Starting a two-player game...")
    try:
        import main  # Import your main game logic
        main.main()  # Pass the mode as a parameter
    except Exception as e:
        print(f"Error starting two-player game: {e}")

# Function to start AI mode

# Function to choose game mode
def choose_game_mode():
    mode_window = tk.Toplevel(window)
    mode_window.title("Choose Game Mode")
    mode_window.geometry("1000x900")  # Match main window size
    mode_window.configure(bg="pink")

    tk.Label(mode_window, text="Select Game Mode", font=("Arial", 28), bg="pink", fg="white").pack(pady=20)

    two_player_button = tk.Button(
        mode_window,
        text="Two Player Mode",
        font=("Arial", 28),
        bg="pink",
        fg="black",
        command=lambda: [mode_window.destroy(), start_two_player_game()]
    )
    two_player_button.pack(pady=20)


# Function for settings
def settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("1000x900")  # Match main window size
    settings_window.configure(bg="pink")  # Match main window background color

    def play_music():
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

    def pause_music():
        pygame.mixer.music.pause()

    def resume_music():
        pygame.mixer.music.unpause()

    def stop_music():
        pygame.mixer.music.stop()

    def adjust_volume(value):
        pygame.mixer.music.set_volume(float(value) / 100)

    tk.Label(settings_window, text="Music Controls", font=("Arial", 16), bg="pink").pack(pady=10)

    play_button = tk.Button(settings_window, text="Play Music", font=("Arial", 16), bg="pink", fg="black", command=play_music)
    play_button.pack(pady=5)

    pause_button = tk.Button(settings_window, text="Pause Music", font=("Arial", 16), bg="pink", fg="black", command=pause_music)
    pause_button.pack(pady=5)

    resume_button = tk.Button(settings_window, text="Resume Music", font=("Arial", 16), bg="pink", fg="black", command=resume_music)
    resume_button.pack(pady=5)

    stop_button = tk.Button(settings_window, text="Stop Music", font=("Arial", 16), bg="pink", fg="black", command=stop_music)
    stop_button.pack(pady=5)

    volume_label = tk.Label(settings_window, text="Volume", font=("Arial", 16), bg="pink")
    volume_label.pack(pady=5)

    volume_slider = tk.Scale(
        settings_window,
        from_=0,
        to=100,
        orient="horizontal",
        command=adjust_volume,
        bg="pink",
        length=200
    )
    volume_slider.set(50)  # Default volume
    volume_slider.pack(pady=10)

# Function to exit the application
def exit_app():
    result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if result:
        window.destroy()
        pygame.mixer.quit()

# Create the main window
window = tk.Tk()
window.title("Chess Game")
window.geometry("1000x900")  # Set the window size

# Set the background color of the main window to pink
window.configure(bg="pink")

# Title label
title_label = tk.Label(window, text="Chess Game", font=("Arial", 48), bg="pink", fg="white")
title_label.pack(pady=20)

# Create and place buttons with pink background
play_button = tk.Button(window, text="Play Game", font=("Arial", 28), bg="pink", fg="black", command=choose_game_mode)
play_button.pack(pady=10)

settings_button = tk.Button(window, text="Settings", font=("Arial", 28), bg="pink", fg="black", command=settings)
settings_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", font=("Arial", 28), bg="pink", fg="black", command=exit_app)
exit_button.pack(pady=10)

# Start the main loop
window.mainloop()