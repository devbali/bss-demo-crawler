#ffmpeg extract frames

import subprocess
import os
import time

def run_get_frames(filename, sec_gap=1, current_frame=0):
  serial_number = 1
  while True:
    outfile = f"frames/{serial_number: 05}.out_{current_frame}.bmp"
    subprocess.call(["ffmpeg", "-i", filename, "-ss", f"{current_frame}", "-frames:v", "1", outfile])
    if os.path.exists(outfile):
      print("Added new frame", outfile)
      current_frame += sec_gap
      serial_number += 1
    else:
      sleep_time = sec_gap/2
      print(f"Up to date, sleeping for {sleep_time} seconds")
      time.sleep(sleep_time)

if __name__ == "__main__":
  filename = list(filter(lambda name: ".mp4.part" in name, os.listdir(".")))[0]
  run_get_frames(filename)
