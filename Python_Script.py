import datetime

# Generate a timestamp to use in the filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the content to write to the file
content = "This is some content that will be written to the file."

# Define the filename using the timestamp
filename = f"output_{timestamp}.txt"

# Write the content to the file
with open(filename, "w") as file:
    file.write(content)

print(f"Content has been written to {filename}")
