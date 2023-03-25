from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def download_audio():
    # Get the YouTube URL from the user input
    url = url_entry.get()

    # Download the video
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        filename = video.default_filename
        video.download()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    # Convert the video to MP3
    try:
        clip = AudioFileClip(filename)
        default_name = filename.split('.')[0]
        output_file = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                   initialfile=f"{default_name}.mp3")
        clip.write_audiofile(output_file)
        clip.close()
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Delete the downloaded video
    os.remove(filename)

# Create the GUI window
window = tk.Tk()
window.title("YouTube to MP3 Converter")

# Set the window size and center it on the screen
window_width = 400
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set the window icon
window.iconbitmap("youtube.ico")

# Create a label for the title
title_label = tk.Label(window, text="YouTube to MP3 Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=(20, 10))

# Create the URL input field
url_label = tk.Label(window, text="Enter the YouTube URL:")
url_label.pack(pady=(10, 5))
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=(0, 10))

# Create the download button
download_button = tk.Button(window, text="Download", command=download_audio, width=10)
download_button.pack()

# Run the GUI loop
window.mainloop()
