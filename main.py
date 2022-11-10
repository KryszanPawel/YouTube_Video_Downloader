from pytube import YouTube, exceptions
import tkinter as tk
from tkinter import filedialog

base_font = ("Baskerville", 10, "")


def browse():
    file_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    browse_label.config(text=f"Chosen directory: {file_dir}")
    browse_dialog.config(text="Change")


def download_start():
    dir = browse_label.cget("text").replace("Chosen directory: ", "", )
    if dir not in ["Choose download directory.", "Please choose correct directory.", ""]:
        root.title('Downloading...')
        root.after(100, download)
    else:
        browse_label.config(text="Please choose correct directory.")


def download():
    dir = browse_label.cget("text").replace("Chosen directory: ", "", )
    url = url_input.get()
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(dir)
        root.title('Download complete. Ready for next video')
        url_input.delete(0, "end")
        url_input.insert(0, "Insert link here")
    except exceptions.RegexMatchError:
        root.title('Video not found.')



def click(event):
    url_input.delete(0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Youtube Downloader')

    window_width = 400
    window_height = 250

    # TODO center window on screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(width=False, height=False)

    # TODO UI HAS TO LOOK DECENT
    # root.iconbitmap("./images_and_icons/youtube.png")

    greeting = tk.Label(text="Youtube video downloader", font=("Helvetica", 20, "bold"))
    greeting.grid(row=0, column=0, columnspan=2, pady=5, padx=15)

    # URL

    url_label = tk.Label(text="Paste video url to download.", font=base_font, width=22)
    url_label.grid(row=1, column=0, sticky='w', padx=11, pady=5)

    url_input = tk.Entry(font=base_font, width=22)
    url_input.insert(0, "Insert link here")
    url_input.bind("<Button-1>", click)
    url_input.grid(row=1, column=1, sticky="w")

    # BROWSE

    browse_label = tk.Label(text="Choose download directory.", font=base_font, width=45, wraplength=390)
    browse_label.grid(row=2, column=0, columnspan=2, pady=5)

    browse_dialog = tk.Button(text="Browse", command=browse, font=base_font, width=42)
    browse_dialog.grid(row=3, column=0, columnspan=2, pady=5)

    # DOWNLOAD

    button = tk.Button(text="Download", command=download_start, width=42, font=base_font)
    button.grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()
