import datetime
import os

# Directory to save the file
directory = "files"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a file with the timestamp as its name in the directory
file_path = os.path.join(directory, f"{timestamp}.txt")
with open(file_path, "w") as file:
    file.write("This file was created at: " + timestamp)
