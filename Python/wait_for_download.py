import time
import os

def wait_for_download(download_dir, timeout=30):
    seconds = 0
    while seconds < timeout:
        files = os.listdir(download_dir)
        downloading = [f for f in files if f.endswith(".part") or f.endswith(".crdownload")]
        if not downloading:
            return True
        time.sleep(1)
        seconds += 1
    return False
