import datetime

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a file with the timestamp as its name
file_name = f"{timestamp}.txt"
with open(file_name, "w") as file:
    file.write("This file was created at: " + timestamp)
