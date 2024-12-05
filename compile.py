import os
import re
from datetime import datetime

# Function to extract the date from the metadata at the top of the file
def extract_date_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to find the date
    date_pattern = r'Date:\s([0-9/]+)\s(\d{2}:\d{2})'
    match = re.search(date_pattern, content)
    
    if match:
        # Combine date and time to create a datetime object
        date_str = match.group(1) + " " + match.group(2)
        return datetime.strptime(date_str, "%m/%d/%Y %H:%M")
    
    return None

# Function to extract "Cool Stuff" section from a file
def extract_cool_stuff_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Search for "Cool Stuff" section
    cool_stuff_section = ""
    cool_stuff_pattern = r'##\sCool Stuff\s*(.*?)\n(?=##|$)'
    match = re.search(cool_stuff_pattern, content, flags=re.DOTALL)
    
    if match:
        cool_stuff_section = match.group(1).strip()
    
    return cool_stuff_section

# Function to get all markdown files in a directory
def get_markdown_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]

# Function to create combined markdown for "Cool Stuff" section
def create_combined_cool_stuff(files, output_file):
    combined_content = "# Combined Cool Stuff\n\n"
    
    # List to store all cool stuff items with their date
    cool_stuff_items = []
    
    # Iterate over files and extract the cool stuff
    for file in files:
        file_date = extract_date_from_file(file)
        if file_date:
            cool_stuff_content = extract_cool_stuff_from_file(file)
            if cool_stuff_content.strip():  # Only add non-empty "Cool Stuff" sections
                cool_stuff_items.append({
                    "date": file_date,
                    "content": cool_stuff_content
                })
    
    # Sort the cool stuff items by date (chronologically)
    cool_stuff_items.sort(key=lambda x: x["date"])
    
    # Combine all cool stuff content into a list format
    combined_content += "- " + "\n- ".join([item["content"] for item in cool_stuff_items]) + "\n"
    
    # Write the combined markdown to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(combined_content)

# Main execution
if __name__ == "__main__":
    # Specify the folder containing markdown files
    folder_path = "./content"  # Change this to the folder with your markdown files
    
    # Get all markdown files in the folder
    markdown_files = get_markdown_files(folder_path)
    
    # Specify output file
    output_filename = "combined_cool_stuff.md"
    
    # Create combined markdown document
    create_combined_cool_stuff(markdown_files, output_filename)
    
    print(f"Combined Cool Stuff markdown report has been saved to '{output_filename}'.")
