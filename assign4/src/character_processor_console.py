import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fetch_block import fetch_block
from processor import process_text

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/blocks.txt")

def load_blocks_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
        
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def display_blocks(block_names):
    print("\nChosen Blocks in Sequence:")
    
    for index, block in enumerate(block_names, start=1):
        print(f"{index}. {block}")

def process_user_input(block_names):
    user_text = input("\nEnter text to process: ")
    
    blocks = [fetch_block(block_name) for block_name in block_names]
    
    return process_text(user_text, *blocks)

def main():
    block_names = load_blocks_from_file(DATA_FILE)
    
    if not block_names:
        return
    
    display_blocks(block_names)
    
    processed_text = process_user_input(block_names)
    
    print(f"\nProcessed Text:\n{processed_text}")

if __name__ == "__main__":
    main()
