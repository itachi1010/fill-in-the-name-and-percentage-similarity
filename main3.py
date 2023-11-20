import os
import re
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def extract_similarity_info(pdf_path):
    with fitz.open(pdf_path) as pdf_doc:
        text = ""
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc[page_num]
            text += page.get_text()

        # Extract similarity information using regex
        match = re.search(r'SIMILARITY INDEX: (\d+)%', text)
        if match:
            similarity_percentage = match.group(1)
            return similarity_percentage
        else:
            return None

def create_similarity_file(pdf_folder):
    with open('similarity_file.txt', 'w') as file:
        for pdf_file in os.listdir(pdf_folder):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder, pdf_file)
                similarity_percentage = extract_similarity_info(pdf_path)

                if similarity_percentage is not None:
                    # Prepend "00" to the file name
                    paper_name = f"00{pdf_file[:-4]}"  # Remove ".pdf" extension
                    line = f'"{paper_name}", {similarity_percentage}% similarity\n'
                    file.write(line)
                else:
                    print(f"No similarity information found for {pdf_file}")

    print("File created successfully: similarity_file.txt")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory(title="Select the folder containing PDFs")
    return folder_selected

# Ask the user to select the folder
pdf_folder_path = select_folder()

# Run the function
create_similarity_file(pdf_folder_path)
