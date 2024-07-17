import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("YouTube Downloader")
        self.geometry("400x350")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Link input
        tk.Label(self, text="YouTube Link:").grid(row=0, column=0, padx=10, pady=10)
        self.link_entry = tk.Entry(self, width=50)
        self.link_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Quality options
        tk.Label(self, text="Quality:").grid(row=1, column=0, padx=10, pady=10)
        self.quality_var = tk.StringVar()
        self.quality_menu = ttk.Combobox(self, textvariable=self.quality_var)
        self.quality_menu['values'] = ('144p', '240p', '360p', '480p', '720p', '1080p')
        self.quality_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # Audio/Video options
        tk.Label(self, text="Type:").grid(row=2, column=0, padx=10, pady=10)
        self.type_var = tk.StringVar()
        self.type_menu = ttk.Combobox(self, textvariable=self.type_var)
        self.type_menu['values'] = ('Video', 'Audio')
        self.type_menu.grid(row=2, column=1, padx=10, pady=10)
        
        # File format options
        tk.Label(self, text="File Format:").grid(row=3, column=0, padx=10, pady=10)
        self.format_var = tk.StringVar()
        self.format_menu = ttk.Combobox(self, textvariable=self.format_var)
        self.format_menu['values'] = ('mp4', 'mkv', 'mp3')
        self.format_menu.grid(row=3, column=1, padx=10, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Download button
        self.download_button = tk.Button(self, text="Download", command=self.download)
        self.download_button.grid(row=5, column=1, pady=20)
        
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes')
            downloaded = d.get('downloaded_bytes')
            if total and downloaded:
                percent = int(downloaded / total * 100)
                self.progress['value'] = percent
                self.update_idletasks()
        
    def download(self):
        link = self.link_entry.get()
        quality = self.quality_var.get()
        file_type = self.type_var.get()
        file_format = self.format_var.get()
        
        if not link or not quality or not file_type or not file_format:
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            download_path = filedialog.askdirectory()
            if not download_path:
                return

            ydl_opts = {
                'format': f'bestvideo[height<={quality[:-1]}]+bestaudio/best',
                'outtmpl': f'{download_path}/%(title)s.%(ext)s',
                'merge_output_format': file_format,
                'ffmpeg_location': r'C:\ffmpeg\bin',  # Adjust this path to where ffmpeg is located on your system
                'quiet': True,
                'progress_hooks': [self.progress_hook],
            }
            if file_type == 'Audio':
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': file_format,
                    'preferredquality': '192',
                }]
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            messagebox.showinfo("Success", f"Downloaded to {download_path}")
        except yt_dlp.utils.DownloadError as e:
            messagebox.showerror("Error", f"Download error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        finally:
            self.progress['value'] = 0

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
