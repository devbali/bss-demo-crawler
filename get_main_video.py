import sys

sys.path.append("./yt-dlp")

import yt_dlp

def run_get_video (youtube_url, output_filename):
  ydl_opts = {
    "forceprint": ["urls"],
    "format": 'm4a/bestvideo',
    "outtmpl": output_filename
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download([youtube_url])

if __name__ == "__main__":
  youtube_url = "https://www.youtube.com/watch?v=CXJbVU3vNzQ"
  run_get_video(youtube_url, "out.mp4")
