import os
import fnmatch
import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar
from pygame import mixer

# Initialize mixer
mixer.init()

# Function to search for MP3 files
def search_files(directory, extension="mp3"):
    mp3_files = []
    for root, _, files in os.walk(directory):
        for file in fnmatch.filter(files, f"*.{extension}"):
            mp3_files.append(os.path.join(root, file))
    return mp3_files

# Function to browse for a directory
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        update_song_list(directory)

# Function to update the song list
def update_song_list(directory):
    global mp3_list
    mp3_list = search_files(directory)
    song_list.delete(0, tk.END)
    for file in mp3_list:
        song_list.insert(tk.END, os.path.basename(file))

# Function to play the selected song
def play_song():
    try:
        selected_index = song_list.curselection()[0]
        selected_file = mp3_list[selected_index]
        mixer.music.load(selected_file)
        mixer.music.set_volume(0.7)
        mixer.music.play()
    except IndexError:
        status_label.config(text="No song selected!")

# Function to pause
def pause_song():
    mixer.music.pause()

# Function to resume
def resume_song():
    mixer.music.unpause()

# Function to stop
def stop_song():
    mixer.music.stop()

# Function to change volume
def set_volume(val):
    mixer.music.set_volume(float(val))

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x400")

# Buttons
browse_button = tk.Button(root, text="Browse Folder", command=browse_directory)
browse_button.pack()

# Song Listbox with Scrollbar
scrollbar = Scrollbar(root)
song_list = Listbox(root, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
scrollbar.config(command=song_list.yview)
song_list.pack(fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Playback buttons
play_button = tk.Button(root, text="Play", command=play_song)
pause_button = tk.Button(root, text="Pause", command=pause_song)
resume_button = tk.Button(root, text="Resume", command=resume_song)
stop_button = tk.Button(root, text="Stop", command=stop_song)

play_button.pack()
pause_button.pack()
resume_button.pack()
stop_button.pack()

# Volume slider
volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=set_volume)
volume_slider.set(0.7)
volume_slider.pack()

# Status label
status_label = tk.Label(root, text="Select a folder to load songs.")
status_label.pack()

# Run the application
root.mainloop()
