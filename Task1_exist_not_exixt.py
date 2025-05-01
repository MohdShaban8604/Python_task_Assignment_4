try:
    # Open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print each line in the file
        print("Raeding file content")

        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}") # Use strip() to remove extra newline characters
except FileNotFoundError:
    # Handle the error if the file does not exist
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Handle other unexpected errors
    print(f"An unexpected error occurred: {e}")