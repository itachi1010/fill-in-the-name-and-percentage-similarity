def create_similarity_file():
    start_number = int(input("Enter the starting number: "))
    end_number = int(input("Enter the ending number: "))

    with open('similarity_file.txt', 'w') as file:
        for i in range(start_number, end_number + 1):
            paper_name = f"00{i}"  # Prepend "00" to the current number
            similarity_percentage = input(f"Enter the percentage similarity for Paper {paper_name}: ")

            line = f'"{paper_name}", {similarity_percentage}% similarity\n'
            file.write(line)

    print("File created successfully: similarity_file.txt")

# Run the function
create_similarity_file()
