import subprocess
import threading
import time
import os

# Function to install Java
def install_java():
    print("Installing Java...")
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y", "openjdk-11-jre-headless"])
    print("Java installed.")

# Function to start Lavalink
def start_lavalink():
    subprocess.run(["java", "-jar", "Lavalink.jar"])

# Function to start Flask application
def start_flask():
    subprocess.run(["python", "status_app.py"])

# Install Java if not already installed
if not os.system("java -version"):
    install_java()

# Download Lavalink.jar if not already present
subprocess.run(["python", "download_lavalink.py"])

# Start Lavalink in a new thread
lavalink_thread = threading.Thread(target=start_lavalink)
lavalink_thread.start()

# Give Lavalink some time to start (adjust as necessary)
time.sleep(10)

# Start Flask application in the main thread
start_flask()
