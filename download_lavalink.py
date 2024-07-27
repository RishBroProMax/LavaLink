import urllib.request
import os

def download_lavalink():
    url = "https://github.com/freyacodes/Lavalink/releases/latest/download/Lavalink.jar"
    output_path = "Lavalink.jar"

    if not os.path.exists(output_path):
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, output_path)
        print(f"Lavalink.jar downloaded to {output_path}")
    else:
        print("Lavalink.jar already exists, skipping download.")

if __name__ == "__main__":
    download_lavalink()
