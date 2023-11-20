def create_similarity_file():
    num_papers = int(input("Enter the number of papers: "))

    with open('similarity_file.txt', 'w') as file:
        for i in range(1, num_papers + 1):
            paper_name = input(f"Enter the name of Paper {i}: ")
            similarity_percentage = input(f"Enter the percentage similarity for Paper {i}: ")

            line = f'"{paper_name}", {similarity_percentage}% similarity\n'
            file.write(line)

    print("File created successfully: similarity_file.txt")


# Run the function
create_similarity_file()
