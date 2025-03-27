import sys
from process_text import process_text
from spell_check import is_spelling_correct

def main(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            processed_text = process_text(text, is_spelling_correct)
            print(processed_text)
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_ui.py <filename>")
    else:
        main(sys.argv[1])
