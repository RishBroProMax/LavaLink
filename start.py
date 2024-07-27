import subprocess
import threading
import time

# Function to start Lavalink
def start_lavalink():
    subprocess.run(["java", "-jar", "Lavalink.jar"])

# Function to start Flask application
def start_flask():
    subprocess.run(["python", "status_app.py"])

# Download Lavalink.jar if not already present
subprocess.run(["python", "download_lavalink.py"])

# Start Lavalink in a new thread
lavalink_thread = threading.Thread(target=start_lavalink)
lavalink_thread.start()

# Give Lavalink some time to start (adjust as necessary)
time.sleep(10)

# Start Flask application in the main thread
start_flask()
