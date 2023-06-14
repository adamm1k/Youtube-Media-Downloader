from pytube import YouTube, Playlist
from tkinter import messagebox, filedialog
import customtkinter

def download_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution stream
        stream = video.streams.get_highest_resolution()

        # Ask the user to select a download location
        save_path = filedialog.asksaveasfilename(defaultextension='.mp4')

        if save_path:
            # Download the video
            stream.download(output_path=save_path)
            return True
        else:
            return False
    except Exception as e:
        print("Error:", str(e))
        return False

def download_playlist(playlist_url):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Ask the user to select a download location for the playlist
        save_path = filedialog.askdirectory()

        if save_path:
            for video_url in playlist.video_urls:
                # Download each video in the playlist
                success = download_video(video_url)
                if not success:
                    messagebox.showwarning("Download Failed", f"Failed to download video: {video_url}")

            messagebox.showinfo("Download Complete", "Playlist downloaded successfully!")
        else:
            messagebox.showwarning("No Location Selected", "Please select a download location.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_download():
    url = url_entry.get()

    if "/playlist" in url:
        download_playlist(url)
    else:
        success = download_video(url)
        if success:
            messagebox.showinfo("Download Complete", "Video downloaded successfully!")

# Create the GUI window and icon
window = customtkinter.CTk()
window.geometry("600x400")
window.iconbitmap(r"C:\Users\theli\Downloads\snagmain_F5T_icon.ico")
                  

#GUI top portions
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
window.title("SnagThis!")

# URL entry field
url_label = customtkinter.CTkLabel(window, text="Video/Playlist URL:")
url_label.pack()
url_entry = customtkinter.CTkEntry(window, width=500)
url_entry.pack()


# Download button
download_button = customtkinter.CTkButton(window, text="Download", command=handle_download)
download_button.pack()

# Start the GUI event loop
window.mainloop()


