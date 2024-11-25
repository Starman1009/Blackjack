import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Define the file path
file_path = "test.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File {file_path} does not exist.")
else:
    try:
        with open(file_path, "r+") as f:
            print(f"File {file_path} opened successfully.")
            # Read the content of the file
            content = f.read()
            print("File content:", content)
            # Perform other file operations here
    except Exception as e:
        print(f"An error occurred: {e}")