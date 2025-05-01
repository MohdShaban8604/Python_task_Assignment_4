# Step 1: Take user input and write to the file
with open('output.txt', 'w') as file:
    user_input = input("Enter some text to write to the file: ")
    file.write(user_input + '\n')
    print("Data successfully written to output.txt.\n")


# Step 2: Append more data to the same file
with open('output.txt', 'a') as file:
    additional_input = input("Enter additional text to append : ")
    file.write(additional_input + '\n')
    print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt :")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.strip())