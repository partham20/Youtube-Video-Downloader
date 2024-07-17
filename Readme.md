# YouTube Downloader

A simple and efficient YouTube downloader built with Python and Tkinter, allowing you to download YouTube videos and audio with ease. This application supports downloading in various qualities and formats including mp4, mkv, and mp3.

## Features

- **Download Videos and Audio**: Choose between video and audio download options.
- **Multiple Quality Options**: Select desired video quality (144p, 240p, 360p, 480p, 720p, 1080p).
- **Various Formats**: Download files in mp4, mkv, or mp3 formats.
- **Progress Bar**: Visual feedback on the download progress.

## Requirements

- Python 3.x
- yt-dlp
- tkinter
- ffmpeg

## Installation

1. **Clone the repository**:

    ```bash
    git https://github.com/partham20/Youtube-Video-Downloader.git
    cd youtube-downloader
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install ffmpeg**:

    - Download and install ffmpeg from [FFmpeg official website](https://ffmpeg.org/download.html).
    - Add ffmpeg to your system's PATH.

## Usage

1. **Run the application**:

    ```bash
    python youtube_downloader.py
    ```

2. **Enter the YouTube link**, select the desired quality, type (Video or Audio), and file format.

3. **Click the "Download" button** and choose the directory where you want to save the downloaded file.

## Project Structure

```plaintext
youtube-downloader/
│
├── youtube_downloader.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - A youtube-dl fork with additional features and fixes.
- [ffmpeg](https://ffmpeg.org/) - A complete, cross-platform solution to record, convert and stream audio and video.

## Contact

For any questions or suggestions, feel free to open an issue or contact me directly at parthasarathym20@gmail.com.

---

Happy downloading! 🎉
