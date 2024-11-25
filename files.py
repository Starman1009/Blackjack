file_path = r"C:\whatthe\Blackjack\test.txt"  # Use raw string to avoid escape sequences

try:
    with open(file_path, "r+") as f:
        print(f"File {file_path} opened successfully.")
        # Read the content of the file
        content = f.read()
        print("File content:", content)
        # Perform other file operations here
except Exception as e:
    print(f"An error occurred: {e}")